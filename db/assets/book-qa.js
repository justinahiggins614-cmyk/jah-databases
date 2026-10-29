/* LJBookQA — per-book Q&A for the Library of Jerusalem.
 *
 * Answers ONLY from the book on this page: its title page, its chapters
 * and its appendices (the [data-audio-text] sections). Every answer is a
 * verbatim sentence from the page, labeled with the section it came from.
 * When no sentence in the book matches the question, the box says plainly
 * that the book does not contain the answer. Nothing is invented, no
 * outside data is consulted, no network call is made, no key is baked in.
 *
 * The assistant on each page presents itself under an associated angel
 * name (see angel-map.json): named in honor of that angel; this program
 * is not the angel.
 */
(function (global) {
  'use strict';

  var STOP = {
    a: 1, an: 1, the: 1, and: 1, or: 1, of: 1, to: 1, in: 1, on: 1, for: 1,
    is: 1, are: 1, was: 1, were: 1, be: 1, by: 1, with: 1, what: 1, how: 1,
    why: 1, when: 1, where: 1, who: 1, which: 1, does: 1, do: 1, did: 1,
    can: 1, could: 1, should: 1, would: 1, it: 1, its: 1, this: 1, that: 1,
    these: 1, those: 1, there: 1, here: 1, from: 1, about: 1, into: 1,
    than: 1, then: 1, so: 1, as: 1, at: 1, i: 1, me: 1, my: 1, you: 1,
    your: 1, tell: 1, please: 1, book: 1
  };

  function tokens(text) {
    var out = [];
    var words = (text || '').toLowerCase().match(/[a-z0-9]+/g) || [];
    for (var i = 0; i < words.length; i++) {
      if (!STOP[words[i]] && out.indexOf(words[i]) === -1) out.push(words[i]);
    }
    return out;
  }

  function nodeText(node) {
    return (node.textContent || '').replace(/\s+/g, ' ').trim();
  }

  /* Split text into sentences, keeping the punctuation. */
  function splitSentences(text) {
    var m = (text || '').match(/[^.!?]+[.!?]+["']?/g) || [];
    var out = [];
    for (var i = 0; i < m.length; i++) {
      var s = m[i].replace(/\s+/g, ' ').trim();
      if (s.length > 0) out.push(s);
    }
    return out;
  }

  /* Build the searchable sections of a document-like object. */
  function buildSections(doc) {
    var sections = [];
    var h1 = doc.querySelector ? doc.querySelector('h1') : null;
    var title = h1 ? nodeText(h1) : '';
    var kv = doc.querySelector ? doc.querySelector('.kv') : null;
    var titleText = title + (kv ? ' ' + nodeText(kv) : '');
    if (titleText.trim()) sections.push({ label: 'Title page', text: titleText });
    var nodes = doc.querySelectorAll ? doc.querySelectorAll('[data-audio-text]') : [];
    for (var i = 0; i < nodes.length; i++) {
      var h = nodes[i].querySelector ? nodes[i].querySelector('h2') : null;
      var label = h ? nodeText(h) : ('Section ' + (i + 1));
      sections.push({ label: label, text: nodeText(nodes[i]) });
    }
    return sections;
  }

  /* Answer a question from sections only. Returns {found, answers, note}.
   * answers are verbatim sentences with their section label. */
  function answerQuestion(sections, question) {
    var q = tokens(question);
    if (q.length === 0) {
      return { found: false, answers: [], note: 'Please ask a question about something in this book.' };
    }
    var best = [];
    for (var s = 0; s < sections.length; s++) {
      var sentences = splitSentences(sections[s].text);
      for (var i = 0; i < sentences.length; i++) {
        var st = tokens(sentences[i]);
        var matched = 0;
        for (var k = 0; k < q.length; k++) {
          if (st.indexOf(q[k]) !== -1) matched++;
        }
        if (matched > 0) best.push({ score: matched, order: s * 100000 + i, sentence: sentences[i], label: sections[s].label });
      }
    }
    if (best.length === 0) {
      return { found: false, answers: [], note: 'This book does not contain an answer to that question.' };
    }
    best.sort(function (x, y) { return (y.score - x.score) || (x.order - y.order); });
    var top = best.slice(0, 2);
    return { found: true, answers: top, note: '' };
  }

  var api = {
    tokens: tokens, splitSentences: splitSentences,
    buildSections: buildSections, answerQuestion: answerQuestion
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.LJBookQA = api;

  if (typeof document !== 'undefined' && typeof window !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      var askBtn = document.getElementById('lj-qa-ask');
      var input = document.getElementById('lj-qa-input');
      var out = document.getElementById('lj-qa-answer');
      if (!askBtn || !input || !out) return;
      function render(res) {
        if (!res.found) {
          out.textContent = res.note;
          return;
        }
        var html = '';
        for (var i = 0; i < res.answers.length; i++) {
          html += '<p>' + res.answers[i].sentence + ' <em>(' + res.answers[i].label + ')</em></p>';
        }
        out.innerHTML = html;
      }
      function ask() {
        var q = input.value || '';
        var sections = buildSections(document);
        render(answerQuestion(sections, q));
      }
      askBtn.addEventListener('click', ask);
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') ask();
      });
    });
  }
})(typeof window !== 'undefined' ? window : globalThis);
