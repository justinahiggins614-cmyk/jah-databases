/* LJDownload — per-book download for the Library of Jerusalem.
 *
 * Collects the book's own page content — title page line, every chapter
 * section and every appendix section, in page order — and downloads it as
 * one plain-text file the reader's phone can save. Client-side only: no
 * server, no network, no new backend. The text comes from the page itself,
 * so the download can never disagree with the book on screen.
 *
 * Sections are the [data-audio-text] elements (chapters + appendices),
 * the same nodes the read-aloud player reads from.
 */
(function (global) {
  'use strict';

  function nodeText(node) {
    return (node.textContent || '').replace(/\s+/g, ' ').trim();
  }

  function sectionHeading(node) {
    var h = null;
    if (node.querySelector) h = node.querySelector('h2');
    return h ? nodeText(h) : '';
  }

  /* Pure collection: returns the full download text for a document-like
   * object with querySelector / querySelectorAll. Testable in node with
   * a fake document built from page HTML. */
  function collectDownloadText(doc, bookId) {
    var parts = [];
    var h1 = doc.querySelector ? doc.querySelector('h1') : null;
    var title = h1 ? nodeText(h1) : '';
    if (title) parts.push(title);
    if (bookId) parts.push('Book ID: ' + bookId);
    var nodes = doc.querySelectorAll ? doc.querySelectorAll('[data-audio-text]') : [];
    for (var i = 0; i < nodes.length; i++) {
      var head = sectionHeading(nodes[i]);
      var body = nodeText(nodes[i]);
      if (head && body.indexOf(head) === 0) body = body.slice(head.length).trim();
      if (head) parts.push('## ' + head);
      if (body) parts.push(body);
    }
    return parts.join('\n\n');
  }

  function downloadBook(doc, bookId) {
    var text = collectDownloadText(doc, bookId);
    var blob = new global.Blob([text], { type: 'text/plain;charset=utf-8' });
    var url = global.URL.createObjectURL(blob);
    var a = doc.createElement('a');
    a.href = url;
    a.download = (bookId || 'book') + '.txt';
    doc.body.appendChild(a);
    a.click();
    doc.body.removeChild(a);
    global.URL.revokeObjectURL(url);
    return text;
  }

  var api = { collectDownloadText: collectDownloadText, downloadBook: downloadBook };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.LJDownload = api;

  if (typeof document !== 'undefined' && typeof window !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      var btn = document.getElementById('lj-download');
      if (!btn) return;
      btn.addEventListener('click', function () {
        var status = document.getElementById('lj-download-status');
        var bookId = btn.getAttribute('data-book-id') || '';
        try {
          downloadBook(document, bookId);
          if (status) status.textContent = 'Downloaded ' + (bookId || 'this book') + '.txt';
        } catch (e) {
          if (status) status.textContent = 'Download did not start in this browser. Try a full browser.';
        }
      });
    });
  }
})(typeof window !== 'undefined' ? window : globalThis);
