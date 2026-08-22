from urllib.parse import urlencode

from docutils import nodes
from docutils.parsers.rst import roles
from sphinx import addnodes
from sphinx.environment.adapters import toctree

from . import pygments_override, translator


BLUECONNECT_COMMERCIAL = {
    'blue_connect/overview': {
        'solution': 'blue_connect',
        'intent': 'stack_discovery',
        'title': 'Descubra o stack certo para sua operação',
        'description': 'Leve seu cenário, versão do Odoo e prioridades para um diagnóstico orientado a solução.',
        'primary_label': 'Montar meu diagnóstico',
    },
    'blue_connect/crm_omnichannel': {
        'solution': 'crm_omnichannel',
        'intent': 'implementation',
        'title': 'Valide CRM e Omnichannel no seu Odoo',
        'description': 'Mapeie WhatsApp, Chatwoot, Kanban, Helpdesk e agenda sem duplicar a fonte de verdade.',
        'primary_label': 'Avaliar no meu ambiente',
    },
    'blue_connect/financeiro_asaas': {
        'solution': 'financeiro_asaas',
        'intent': 'implementation',
        'title': 'Valide cobrança, pagamentos e NFSe no seu fluxo',
        'description': 'Confira dependências, meios de pagamento, recorrência e pontos de integração antes da implantação.',
        'primary_label': 'Validar integração financeira',
    },
    'blue_connect/data_intelligence': {
        'solution': 'data_intelligence',
        'intent': 'data_assessment',
        'title': 'Defina as consultas e fontes de dados do seu caso',
        'description': 'Transforme a necessidade de CPF, CNPJ, crédito ou enriquecimento em um fluxo de consulta governado.',
        'primary_label': 'Avaliar meu caso de dados',
    },
    'blue_connect/growth_sales': {
        'solution': 'growth_sales',
        'intent': 'sales_assessment',
        'title': 'Desenhe sua máquina comercial',
        'description': 'Conecte geração, enriquecimento, distribuição, cadência, WhatsApp e CRM em uma jornada mensurável.',
        'primary_label': 'Avaliar minha operação comercial',
    },
    'blue_connect/ai_automation': {
        'solution': 'ai_automation',
        'intent': 'automation_assessment',
        'title': 'Escolha o primeiro processo para automatizar com IA',
        'description': 'Identifique o gargalo de maior impacto e defina o limite entre automação, agente e decisão humana.',
        'primary_label': 'Descobrir meu primeiro gargalo',
    },
    'blue_connect/saas_revenue': {
        'solution': 'saas_revenue',
        'intent': 'saas_assessment',
        'title': 'Desenhe trial, assinatura e provisionamento',
        'description': 'Valide a jornada comercial, cobrança e liberação da instância antes de automatizar o lifecycle.',
        'primary_label': 'Desenhar meu fluxo SaaS',
    },
    'blue_connect/releases_marketplace': {
        'solution': 'marketplace',
        'intent': 'adoption',
        'title': 'Quer adotar uma capability desta release?',
        'description': 'Leve a capability, a versão e o cenário para validar readiness, dependências e implantação.',
        'primary_label': 'Avaliar uma capability',
    },
    'blue_connect/module_index': {
        'solution': 'blueapps',
        'intent': 'stack_discovery',
        'title': 'Monte seu stack BlueApps',
        'description': 'Selecione os módulos pelo problema de negócio e valide compatibilidade, dependências e edição.',
        'primary_label': 'Encontrar módulos para meu cenário',
    },
}


def setup(app):
    app.set_translator('html', translator.BootstrapTranslator)

    app.connect('html-page-context', set_missing_meta)
    app.connect('html-page-context', set_blueconnect_commercial_context)

    app.add_js_file('js/utils.js')  # Keep in first position
    app.add_js_file('js/layout.js')
    app.add_js_file('js/menu.js')
    app.add_js_file('js/page_toc.js')
    app.add_js_file('js/switchers.js')
    app.add_js_file('js/docs_growth.js')

    roles.register_canonical_role('icon', icon_role)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }


def set_missing_meta(app, pagename, templatename, context, doctree):
    if context.get('meta') is None:  # Pages without title (used with `include::`) have no meta
        context['meta'] = {}

    # Blue Connect is Portuguese-first. Keep the language selector usable even when the
    # upstream Odoo context does not populate alternate_languages for our custom deployment.
    current_language = app.config.language or 'pt_BR'
    language_labels = {'pt_BR': 'PT-BR', 'en': 'EN', 'es': 'ES'}
    published_languages = getattr(app.config, 'blueconnect_languages', ['pt_BR', 'en', 'es'])
    context['language'] = language_labels.get(current_language, current_language.upper())
    if not context.get('alternate_languages'):
        page = 'index.html' if pagename == 'index' else f'{pagename}.html'
        context['alternate_languages'] = [
            (
                language_labels.get(code, code.upper()),
                code,
                f'/{page}' if code == 'pt_BR' else f'/{code}/{page}',
            )
            for code in published_languages
            if code != current_language
        ]


def set_blueconnect_commercial_context(app, pagename, templatename, context, doctree):
    commercial = BLUECONNECT_COMMERCIAL.get(pagename)
    if not commercial:
        context['blueconnect_commercial'] = None
        return

    params = {
        'utm_source': 'documentation',
        'utm_medium': 'docs_cta',
        'utm_campaign': 'blueconnect_docs_acquisition',
        'source': 'docs',
        'surface': 'documentation',
        'solution': commercial['solution'],
        'intent': commercial['intent'],
        'page': pagename,
        'version': '19.0',
    }
    context['blueconnect_commercial'] = {
        **commercial,
        'primary_url': f"https://www.conexaoazul.com/diagnostico?{urlencode(params)}",
        'secondary_url': (
            'https://www.conexaoazul.com/blueapps?utm_source=documentation'
            '&utm_medium=docs_cta&utm_campaign=blueconnect_docs_acquisition'
        ),
        'secondary_label': 'Ver BlueApps',
    }


class Monkey:
    """ Replace patched method of an object by a new method receiving the old one in argument. """
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, fn):
        name = fn.__name__
        old = getattr(self.obj, name)
        setattr(self.obj, name, lambda self_, *args, **kwargs: fn(old, self_, *args, **kwargs))


@Monkey(toctree.TocTree)
def resolve(old_resolve, tree, docname, *args, **kwargs):

    def _update_toctree_nodes(_node) -> None:
        """ Make necessary changes to Docutils' nodes of the toc.

        Internal structure of toc nodes:
        <ul>
            <li>
                <p><a/></p>
                <ul>
                    ...
                </ul>
            </li>
            <li/>
        <ul/>
        """
        if isinstance(_node, nodes.reference):  # The node is a reference (<a/>)
            _node_docname = _get_docname(_node)
            _clear_reference_if_empty_page(_node, _node_docname)
            _set_docname_as_class(_node, _node_docname)
        elif isinstance(_node, (addnodes.compact_paragraph, nodes.bullet_list, nodes.list_item)):
            for _subnode in _node.children:
                _update_toctree_nodes(_subnode)

    def _get_docname(_node):
        """ Return the docname of the targeted document.

        docname = some_common_root/foo/bar/the_page_being_rendered
        _ref = ../../contributing/documentation
        _path_parts = ['..', '..', 'contributing', 'documentation']
        _res = ['some_common_root', 'contributing', 'documentation']
        _docname = some_common_root/contributing/documentation

        :return: The docname of the document targeted by `_node`, i.e. the relative path from the
                 documentation source directory (the `content/` directory)
        :rtype: str
        """
        _ref = _node['refuri'].replace('.html', '')
        _parent_directory_occurrences = _ref.count('..')
        if not _parent_directory_occurrences and '/' not in docname:
            _docname = _ref
        else:
            _path_parts = _ref.split('/')
            _res = docname.split('/')[:-(_parent_directory_occurrences+1)] \
                   + _path_parts[_parent_directory_occurrences:]
            _docname = '/'.join(_res)
        return _docname

    def _clear_reference_if_empty_page(_reference_node, _node_docname):
        if _node_docname and any(
            isinstance(_subnode, nodes.bullet_list)
            for _subnode in _reference_node.parent.parent.children
        ):
            if 'show-content' not in tree.env.metadata[_node_docname]:
                _reference_node['refuri'] = '#'

    def _set_docname_as_class(_reference_node, _node_docname):
        _node_docname = _node_docname or docname
        _reference_node.parent.parent['classes'].append(f'o_menu_{_node_docname.replace("/", "_")}')

    resolved_toc = old_resolve(tree, docname, *args, **kwargs)
    if resolved_toc:
        _update_toctree_nodes(resolved_toc)
    return resolved_toc


def icon_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """ Implement an `icon` role for Odoo and Font Awesome icons. """
    for icon_class in text.split():
        if not (icon_class.startswith('fa-') or icon_class.startswith('oi-') \
            or icon_class.startswith('os-')):
            report_error = inliner.reporter.error(
                f"'{icon_class}' is not a valid icon formatting class.", lineno=lineno
            )
            error_node = inliner.problematic(rawtext, rawtext, report_error)
            return [error_node], [report_error]
    if text.startswith('oi-'):
        icon_html = f'<i class="oi {text}"></i>'
    elif text.startswith('fa-'):
        icon_html = f'<i class="fa {text}"></i>'
    elif text.startswith('os-'):
        icon_html = (
            '<svg class="os-icon" aria-hidden="true" role="img">'
                f'<use href="#{text[3:]}" />'
             '</svg>'
        )
    else:
        icon_html = f'<i class="{text}"></i>'
    return [nodes.raw('', icon_html, format='html')], []
