(function () {
    'use strict';

    function pushEvent(payload) {
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push(payload);
        } catch (_) {
            // Analytics must never block documentation navigation.
        }
    }

    function safeSearchTerm(raw) {
        var value = (raw || '').trim().slice(0, 120);
        if (!value) return '';
        if (/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i.test(value)) return '[redacted]';
        if (/\d[\d\s().+\/-]{7,}\d/.test(value)) return '[redacted]';
        return value;
    }

    document.addEventListener('click', function (event) {
        var link = event.target.closest('[data-blueconnect-cta]');
        if (!link) return;
        pushEvent({
            event: 'docs_commercial_intent',
            cta_type: link.getAttribute('data-blueconnect-cta') || 'unknown',
            source: link.getAttribute('data-docs-source') || 'documentation',
            solution: link.getAttribute('data-docs-solution') || '',
            intent: link.getAttribute('data-docs-intent') || '',
            page: link.getAttribute('data-docs-page') || '',
        });
    });

    var commercial = document.querySelector('.ca_docs_growth [data-blueconnect-cta="primary"]');
    if (commercial) {
        pushEvent({
            event: 'docs_solution_view',
            source: 'documentation',
            solution: commercial.getAttribute('data-docs-solution') || '',
            intent: commercial.getAttribute('data-docs-intent') || '',
            page: commercial.getAttribute('data-docs-page') || '',
        });
    }

    var results = document.getElementById('search-results');
    if (!results) return;

    var params = new URLSearchParams(window.location.search);
    var query = safeSearchTerm(params.get('q') || params.get('query') || '');
    if (!query) return;

    var emitted = false;
    function emitSearchDemand() {
        if (emitted) return;
        var links = results.querySelectorAll('a[href]');
        var text = (results.textContent || '').trim().toLowerCase();
        if (!links.length && (!text || text.indexOf('searching') !== -1)) return;
        emitted = true;
        pushEvent({
            event: 'docs_search',
            source: 'documentation',
            search_term: query,
            result_count: links.length,
            has_results: links.length > 0,
        });
    }

    var observer = new MutationObserver(emitSearchDemand);
    observer.observe(results, { childList: true, subtree: true });
    window.setTimeout(function () {
        emitSearchDemand();
        observer.disconnect();
    }, 4000);
})();
