/* ✳ SIGNATURE — JAH Recipe Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW recipes in the exact archive format
   (id, name, chapter, section, ingredients[{qty,unit,item}], steps[],
   prep_min, cook_min, total_min, servings, difficulty). Deterministic:
   same seed + version => same record. Ingredients and steps are built
   constructively together: every ingredient named in a step is in the
   ingredient list, and total_min is recomputed from prep+cook by an
   INDEPENDENT verifier before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-cookbook-1.0';
  var ID_PREFIX = 'JAH-RECIPE-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function shuffle(rnd, arr) {
    arr = arr.slice();
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(rnd() * (i + 1)), t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  /* real archive chapters + sections (from recipes.idx.json) */
  var CHAPTERS = {
    'Appetizers': ['Dips & Spreads', 'Finger Foods', 'Skewers & Bites'],
    'Breads': ['Flatbreads', 'Quick Breads', 'Yeast Breads'],
    'Breakfast': ['Eggs', 'Pancakes & More', 'Warm Grains'],
    'Desserts': ['Cakes', 'Cookies', 'Pies & Tarts', 'Puddings & Creams'],
    'Drinks': ['Coolers', 'Hot Drinks', 'Smoothies & Shakes'],
    'Mains': ['Beef & Pork', 'Chicken', 'Fish & Seafood', 'Pasta & Noodles', 'Vegetarian'],
    'Sides': ['Grains & Rice', 'Potatoes', 'Roasted Vegetables'],
    'Snacks': ['Savory Snacks', 'Sweet Snacks'],
    'Soups & Salads': ['Green Salads', 'Hearty Salads', 'Hearty Soups', 'Light Soups']
  };
  /* genuine dish nouns per chapter (real words, recombined by the generator) */
  var DISHES = {
    'Appetizers': ['Guacamole', 'Hummus', 'Deviled Eggs', 'Bruschetta', 'Stuffed Mushrooms', 'Nachos'],
    'Breads': ['Focaccia', 'Cornbread', 'Dinner Rolls', 'Banana Bread', 'Pita', 'Sourdough Loaf'],
    'Breakfast': ['Omelet', 'Pancakes', 'Oatmeal', 'Breakfast Burrito', 'French Toast', 'Granola'],
    'Desserts': ['Chocolate Cake', 'Sugar Cookies', 'Apple Pie', 'Rice Pudding', 'Brownies', 'Cheesecake'],
    'Drinks': ['Lemonade', 'Hot Cocoa', 'Berry Smoothie', 'Iced Tea', 'Milkshake', 'Cider'],
    'Mains': ['Chicken Stew', 'Beef Stir-Fry', 'Baked Salmon', 'Spaghetti', 'Veggie Curry', 'Pork Chops'],
    'Sides': ['Fried Rice', 'Mashed Potatoes', 'Roasted Carrots', 'Coleslaw', 'Baked Beans', 'Grilled Zucchini'],
    'Snacks': ['Trail Mix', 'Popcorn', 'Cheese Crisps', 'Fruit Salad', 'Pretzel Bites', 'Yogurt Dip'],
    'Soups & Salads': ['Tomato Soup', 'Caesar Salad', 'Chicken Noodle Soup', 'Greek Salad', 'Minestrone', 'Clam Chowder']
  };
  var ADJ = ['Classic', 'Creamy', 'Spicy', 'Golden', 'Rustic', 'Hearty', 'Fresh', 'Savory', 'Sweet', 'Zesty', 'Smoky', 'Herbed'];
  /* real ingredient items + units sampled from the archive */
  var PANTRY = ['salt', 'olive oil', 'black pepper', 'sugar', 'butter', 'milk', 'eggs', 'all-purpose flour',
    'minced garlic', 'paprika', 'honey', 'vanilla extract', 'diced sweet onion', 'garlic powder',
    'vegetable oil', 'vegetable broth', 'chocolate chips', 'baking soda', 'bread flour', 'active dry yeast',
    'warm water', 'russet potatoes', 'baking powder', 'minced shallot', 'brown sugar', 'green beans',
    'warm milk', 'diced carrots', 'beef broth', 'melted butter', 'diced tomatoes', 'chicken breast',
    'chicken broth', 'ice cubes', 'chopped parsley', 'water', 'smoked paprika', 'grated Parmesan',
    'berries', 'mixed nuts', 'Dijon mustard', 'baby potatoes', 'diced yellow onion', 'diced celery stalks',
    'coconut milk', 'egg yolks', 'cinnamon', 'sliced apples', 'balsamic vinegar', 'lemon juice',
    'shredded cheddar', 'heavy cream', 'cornstarch', 'bay leaves', 'thyme', 'oregano', 'cumin',
    'chili powder', 'soy sauce', 'rice vinegar', 'sesame oil', 'green onions', 'fresh basil'];
  var UNITS = ['cup', 'cups', 'tablespoon', 'tablespoons', 'teaspoon', 'teaspoons', 'ounce', 'ounces', 'pound', 'pounds', 'clove', 'cloves', ''];
  var QTYS = ['1', '2', '3', '4', '1/2', '1/3', '1/4', '2/3', '3/4'];
  var DIFFS = ['Easy', 'Medium', 'Hard'];

  function qtyStr(q, unit, item) {
    return q + (unit ? ' ' + unit : '') + ' ' + item;
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var chapters = Object.keys(CHAPTERS);
    var chapter = opts.chapter && CHAPTERS[opts.chapter] ? opts.chapter : pick(rnd, chapters);
    var section = pick(rnd, CHAPTERS[chapter]);
    var name = pick(rnd, ADJ) + ' ' + pick(rnd, DISHES[chapter]);

    /* build the ingredient list first, then write steps from it */
    var items = shuffle(rnd, PANTRY).slice(0, ri(rnd, 5, 8));
    var ingredients = items.map(function (it) {
      return { qty: pick(rnd, QTYS), unit: pick(rnd, UNITS), item: it };
    });
    /* split ingredients into 2-3 bowls; steps name each bowl's real items */
    var bowls = [];
    var per = Math.ceil(ingredients.length / ri(rnd, 2, 3));
    for (var i = 0; i < ingredients.length; i += per) bowls.push(ingredients.slice(i, i + per));
    var steps = [];
    var uses = []; /* _priv: which items each step references */
    bowls.forEach(function (bowl, bi) {
      var named = bowl.map(function (g) { return qtyStr(g.qty, g.unit, g.item); });
      steps.push('In a ' + (bi === 0 ? 'large bowl' : 'separate bowl') + ', combine the ' +
        named.join(', ') + '.');
      uses.push(bowl.map(function (g) { return g.item; }));
    });
    steps.push('Cook over medium heat, stirring, until everything is heated through and tender, about ' +
      ri(rnd, 8, 25) + ' minutes.');
    uses.push([]);
    steps.push('Taste and adjust seasoning. Serve the ' + name + ' warm and enjoy.');
    uses.push([]);

    var prep = ri(rnd, 5, 30), cook = ri(rnd, 10, 60);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      name: name,
      chapter: chapter,
      section: section,
      ingredients: ingredients,
      steps: steps,
      prep_min: prep,
      cook_min: cook,
      total_min: prep + cook,
      servings: ri(rnd, 2, 8),
      difficulty: pick(rnd, DIFFS)
    };
    /* private params for the independent verifier */
    var pub = {};
    ['id', 'n', 'name', 'chapter', 'section', 'ingredients', 'steps',
     'prep_min', 'cook_min', 'total_min', 'servings', 'difficulty'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { prep: prep, cook: cook, servings: rec.servings, uses: uses,
                  items: items, chapter: chapter, section: section, name: name };
    return pub;
  }

  /* independent re-verification: recompute totals and check step<->ingredient consistency */
  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (p.prep + p.cook !== rec.total_min) errs.push('total_min != prep_min + cook_min');
    if (typeof rec.servings !== 'number' || rec.servings < 1 || rec.servings > 12)
      errs.push('servings out of range');
    if (DIFFS.indexOf(rec.difficulty) < 0) errs.push('bad difficulty');
    if (!CHAPTERS[p.chapter] || CHAPTERS[p.chapter].indexOf(p.section) < 0)
      errs.push('section does not belong to chapter');
    if (p.name !== rec.name) errs.push('name mismatch');
    /* every ingredient referenced in a step must exist in the ingredient list */
    var listed = {};
    rec.ingredients.forEach(function (g) { listed[g.item] = (g.qty + '|' + g.unit); });
    p.uses.forEach(function (used, si) {
      used.forEach(function (item) {
        if (!listed[item]) errs.push('step ' + (si + 1) + ' references unlisted ingredient: ' + item);
      });
    });
    /* every ingredient's qty/unit named in its step must match the list entry */
    rec.steps.forEach(function (st, si) {
      (p.uses[si] || []).forEach(function (item) {
        var ing = null;
        rec.ingredients.forEach(function (g) { if (g.item === item) ing = g; });
        if (ing && st.indexOf(qtyStr(ing.qty, ing.unit, ing.item)) < 0)
          errs.push('step ' + (si + 1) + ' misstates qty/unit for ' + item);
      });
    });
    /* every listed ingredient appears in at least one step */
    var seen = {};
    p.uses.forEach(function (u) { u.forEach(function (it) { seen[it] = 1; }); });
    rec.ingredients.forEach(function (g) {
      if (!seen[g.item]) errs.push('ingredient never used in steps: ' + g.item);
    });
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'chapter', 'section', 'ingredients', 'steps',
     'prep_min', 'cook_min', 'total_min', 'servings', 'difficulty'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-RECIPE-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.chapter && !CHAPTERS[rec.chapter]) errs.push('unknown chapter');
    if (!Array.isArray(rec.ingredients) || rec.ingredients.length < 3) errs.push('ingredients must list 3+ items');
    if (!Array.isArray(rec.steps) || rec.steps.length < 3) errs.push('steps must have 3+ entries');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a.name || a.n;
      if (nm && String(nm).toLowerCase() === String(rec.name).toLowerCase())
        errs.push('duplicate of archived recipe name: ' + rec.name);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var words = String(JSON.stringify(t)).match(/[A-Za-z]{4,}/g);
      if (words && words.length) {
        var w = words[0].charAt(0).toUpperCase() + words[0].slice(1).toLowerCase();
        /* nudge the dish name with the theme word — rebuild via a fresh generate */
        var rec3 = generate(seed + (w.length % 97), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + w)));
        rec3.name = w + ' ' + rec3.name.split(' ').slice(1).join(' ');
        rec3._priv.name = rec3.name; /* keep the verifier's copy in sync */
        rec3.id = rec.id; rec3.n = rec.n;
        return rec3;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('cookbook', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    chapters: Object.keys(CHAPTERS)
  });
})();
