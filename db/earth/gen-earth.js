/* ✳ SIGNATURE — JAH Earth Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW address-format PRACTICE records. Every street,
   city and country component is a real component sampled from the stored archive's
   index pools; the combination is newly generated and is ALWAYS labeled a practice
   record — never a verified real address. Deterministic: same seed + version =>
   same record. An independent verifier rebuilds every field from the private
   pool indices before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-earth-1.0';
  var ID_PREFIX = 'JAH-ADDR-';
  var ID_DIGITS = 6;
  var NOTE = 'Generated practice record — address-format drill only. NOT a verified real address.';
  var STAMP = 'JAH Earth Data Base — practice address records in archive format.';
  var STREETS = ["улица Ленина", "Main Street", "Church Street", "امام خمینی", "Carrera 5", "Calle 6", "بلوار امام خمینی", "High Street", "Via Roma", "Calle Benito Juárez", "Carrera 7", "MDR", "Carrera 10", "14a", "Shell", "Rua Sete de Setembro", "3a", "McDonald's", "Calle 8", "Calle 7", "Calle Miguel Hidalgo", "Calle Vicente Guerrero", "Rua Rui Barbosa", "Carrera 4", "Carrera 9", "Avenida Miguel Hidalgo", "Calle 11", "Avenida Getúlio Vargas", "Avenida Central Norte", "Rua Quinze de Novembro", "Rizal Street", "Carrera 6", "Советская улица", "Calle Morelos", "Calle 10", "Rua Castro Alves", "Via Guglielmo Marconi", "Avenida Brasil", "Bridge Street", "Banco do Brasil", "Октябрьская улица", "Market Street", "Subway", "Calle 16 de Septiembre", "Station Road", "2А", "Rua Santo Antônio", "Rue Jean Jaurès", "Calle Abasolo", "King Street", "Atatürk Caddesi", "S203", "Carrera 16", "Avenida Minas Gerais", "Church Road", "Rynek", "East Main Street", "RN1", "Rua Barão do Rio Branco", "Calle Libertad", "Calle 12", "Calle Independencia", "人民路", "Queen Street", "Calle Francisco I. Madero", "Calle 9", "G212", "Calle 3", "2A", "Carrera 8", "Avenida Independencia", "Carrera 12", "24A", "Igreja Matriz", "Breite Straße", "Calle Melchor Ocampo", "6a", "Sunoco", "Calle Mariano Matamoros", "Rathaus", "Сбербанк", "S201", "NH30", "Mahatma Gandhi Road", "22А", "Calle 5", "улица Кирова", "Burgos Street", "2nd Street", "Via Armando Diaz", "Via Giovanni Verga", "State Street", "Via Cesare Battisti", "Садовая улица", "San Martín", "улица Гагарина", "Praça da Matriz", "Well Pharmacy", "Calle 2", "улица Дзержинского", "Calle 4", "Rua Marechal Deodoro da Fonseca", "10A", "Комсомольская улица", "Calle 20", "NH39", "Hùng Vương", "Rua Dom Pedro II", "Plaza Mayor", "Via Giuseppe Mazzini", "North Main Street", "Rua Dez", "улица Калинина", "Via Libertà", "Carrera 13", "Школа №1", "NH20", "A3", "Via Vittorio Veneto", "Rua São Francisco", "Школьная улица", "Calle Central", "Rua Santa Luzia", "Rua Getúlio Vargas", "Via Piave", "Rua Duque de Caxias", "Avenida San Martín", "Citgo", "MSH4", "SH1", "SH2", "GLS", "Rua do Comércio", "خیابان امام خمینی", "Via Alcide De Gasperi", "Rua Tiradentes", "NH17", "SH5", "улица 50 лет Октября", "Rua São Pedro", "Calle 19", "Varanasi - Kanniyakumari Road (Old NH7)", "8a", "A5", "Calle Hidalgo", "Via Milano", "6А", "Пятёрочка", "Rua São José", "Міська рада", "Victoria Road", "X054", "13A", "16A", "A8", "1Б", "Rua General Osório", "Rua Rio Grande do Norte", "Lautaro", "Calle Guillermo Prieto", "Avenida Cuauhtémoc", "Rue de l'Église", "Пролетарская улица", "Pizza Hut", "Via Giuseppe Verdi", "Привокзальная улица", "文昌路", "вулиця Шевченка", "School Road", "Via Papa Giovanni XXIII", "Via Alessandro Manzoni", "NH320G", "Market Square", "Old Provincial Road", "NH15", "A1", "улица 50 лет Победы", "Rua Tupã", "Ощадбанк", "Admiral", "Chacabuco", "Via Dante Alighieri", "1a", "Schulstraße", "Itaú", "Calle de la Iglesia", "Богдана Хмельницького вулиця", "State Farm", "Rua Espírito Santo", "SH10", "EN 250", "Bahnhofstraße", "Avenida Bolívar", "武大线", "Rua Marechal Deodoro", "García Moreno", "28ης Οκτωβρίου", "Avenida Benito Juárez", "Robinson Street", "Calle Central Este", "Jirón Alfonso Ugarte", "Calle 5 de Mayo", "Steyn Street", "Boots", "NH45", "Markt", "Carrera 19", "площадь Ленина", "West El Segundo Boulevard", "Avenida 5 de Mayo", "Первомайская улица", "Sheetz", "Почтовая улица", "Дикси", "NH501", "Hipólito Yrigoyen", "Rua do Olival", "Ozon", "Calle La Paz", "Rue Nationale", "Здравец", "28А", "Park Lane", "和平路", "Grand Trunk Road", "Court Square", "2a", "Avenida Tiradentes", "Grand Avenue", "Calle Francisco Javier Mina", "Sainsbury's Local", "兴隆街", "Via Giordano Bruno", "Van Buren Boulevard", "Maison des Jeunes", "兰海高速", "Avenida Xicohténcatl", "12a", "Austin Conolly Drive", "S518", "Netto Marken-Discount", "Lidl", "Rua Belo Horizonte", "S304", "Quezon Street", "SH4", "проспект Победы", "Avenida Hidalgo", "梁彭路", "23a", "Rua São Sebastião", "Hôtel de Ville", "Центральная улица", "NH7", "San Guillermo Street", "1a Calle", "Adolfo Alsina", "Calle 31", "вулиця Івана Франка", "Arellano Street", "South Main Street", "Front Street", "Calle Santiago", "Avenida Juárez", "N1", "Kolejowa", "Rua Nossa Senhora do Carmo", "台小线", "Via Pasubio", "Rúa da Igrexa", "5B", "Calle 30", "Rua São João", "Hauptstraße", "Noble Street", "Avenue Victor Hugo", "Центральна вулиця", "Police Station", "Avenue de la République", "NH26", "B1", "Rua Dezesseis", "Администрация", "Rua Santa Catarina", "9a", "Paróquia Nossa Senhora Aparecida", "3A", "Via Giovanni Falcone", "Rue de la République", "Rua Marechal Floriano Peixoto", "Main Road", "Avenida Francisco I. Madero", "Sycamore Avenue", "Via San Vincenzo", "Central Road", "Rua Brasil", "Sassandra - Gagnoa", "Union Street", "Rua 7 de Setembro", "Rua do Cruzeiro"];
  var CITIES = ["Centro", "Main Street", "улица Ленина", "Советская улица", "Hauptstraße", "High Street", "Church Street", "East Main Street", "North Main Street", "Октябрьская улица", "Bahnhofstraße", "South Main Street", "Комсомольская улица", "West Main Street", "Washington Street", "Poblacion", "Kirchstraße", "Schulstraße", "Садовая улица", "улица Карла Маркса", "улица Пушкина", "улица Мира", "San Pedro", "Центр", "Пионерская улица", "Downtown", "4th Street", "улица Горького", "Centrum", "Barrio Centro", "Первомайская улица", "Dorpsstraat", "улица Кирова", "Place de l'Église", "Школьная улица", "Lindenstraße", "Barrio El Centro", "Carrer Major", "Broadway", "Adama Mickiewicza", "Central Avenue", "Avenue de la Libération", "8th Street", "Rue de la République", "Восточная улица", "Зелёная улица", "Market Street", "São Sebastião", "Mittelstraße", "San Lorenzo", "Коммунистическая улица", "San Martín", "Mitre", "Hoogstraat", "Ленинская улица", "Santa Isabel", "Park Avenue", "улица Гагарина", "Красноармейская улица", "Rue Jean Jaurès", "Poznańska", "Storgata", "Plac Wolności", "Vicente Guerrero", "Preston", "Rynek", "Altstadt", "Parkstraße", "Вокзальная улица", "Via Michelangelo Buonarroti", "Walnut Street", "Masarykovo náměstí", "Station Road", "Wilhelmstraße", "Elm Street", "East 3rd Street", "San Isidro", "9th Street", "Hauptstrasse", "Партизанская улица", "Thuckalay", "1A", "Rue du Général Leclerc", "Market Place", "Шкільна вулиця", "William Street", "San Juan", "Strada Principală", "Buenos Aires", "1st Avenue", "25 de Mayo", "вуліца Леніна", "Jackson Street", "12th Avenue", "La Loma", "Station Street", "Railroad Street", "Центральна вулиця", "Rue du Parc", "West Washington Street", "Tadeusza Kościuszki", "Bahnhofstrasse", "Stare Miasto", "Lincoln Avenue", "Markt", "Santa Rosa", "Santa Rita", "Садова вулиця", "Kirchgasse", "Marktplatz", "Полевая улица", "улица Володарского", "3rd Street", "Purok 5", "Aurora", "Poststraße", "улица Матросова", "South Street", "Lange Straße", "вулиця Незалежності", "Avenue de la République", "улица Калинина", "Washington Avenue", "The Square", "Beverly Hills", "Rue du Général de Gaulle", "ירושלים", "Kirchplatz", "Santo Antônio", "Alleestraße", "River Street", "Rauhankatu", "Մեսրոպ Մաշտոցի փողոց", "Calle Luis Muñoz Rivera", "улица Тургенева", "Fatima", "Maine Street", "Bennett Avenue", "宁蒗彝族自治县", "Saint-Roch", "Martinstraße", "N 5", "Lübecker Straße", "Центральный округ", "улица Луначарского", "Олександрівка", "West 2nd Street", "Rue du Maréchal Foch", "Union", "Saint-Charles", "Old National Road", "Purok 2", "Zona Centro", "The Crescent", "San Pablo", "Rue Pasteur", "Nørregade", "Jardim Alvorada", "Santo Domingo", "Fairfield", "Forest Hills", "East Washington Street", "Avenida Barão do Rio Branco", "1a", "Миру вулиця", "Cape Town Ward 59", "Ziegelstraße", "La Villa", "Пролетарская улица", "El Bosque", "College Avenue", "London Road", "Centre Vila", "Бердянськ", "Ленінская вуліца", "South Main Avenue", "Ульяновская улица", "State Street", "Hipólito Yrigoyen", "Benito Juárez", "2a", "Avenida Central", "Rue du Centre", "Maple Street", "Loreto", "Pedrinhas", "Commonwealth Avenue", "Thornton", "Beaumont Avenue", "C Street", "Praça da República", "Greenfield Drive", "Villa Unión", "Place de la République", "Rue du Souvenir", "Erlenbachstraße", "城关街道", "Carrera 8", "Wood Street", "Marktstraße"];
  var COUNTRIES = ["Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Aruba", "Australia", "Ayiti", "Azərbaycan", "Barbados", "Belau", "België / Belgique / Belgien", "Belize", "Bermuda", "Bolivia", "Bosna i Hercegovina / Босна и Херцеговина", "Botswana", "Brasil", "Brunei بروني", "Burkina Faso", "Burundi", "Bénin", "Cabo Verde", "Cameroun", "Canada", "Cayman Islands", "Chile", "Colombia", "Comores Komori جزر القمر", "Congo", "Costa Rica", "Crna Gora / Црна Гора", "Cuba", "Curaçao", "Côte d’Ivoire", "Danmark", "Deutschland", "Djibouti جيبوتي", "Dominica", "Ecuador", "Eesti", "El Salvador", "España", "France", "Føroyar", "Gabon", "Gambia", "Ghana", "Gibraltar", "Grenada", "Guatemala", "Guernsey", "Guinea Ecuatorial", "Guiné-Bissau", "Guinée", "Guyana", "Honduras", "Hrvatska", "India", "Indonesia", "Isle of Man", "Italia", "Jamaica", "Kalaallit Nunaat", "Kenya", "Kosova / Kosovo", "Kuzey Kıbrıs", "Ködörösêse tî Bêafrîka / République centrafricaine", "Latvija", "Lesotho", "Liechtenstein", "Lietuva", "Lëtzebuerg", "Madagasikara / Madagascar", "Magyarország", "Malawi", "Malaysia", "Mali", "Malta", "Maroc ⵍⵎⵖⵔⵉⴱ المغرب", "Mauritanie موريتانيا", "Mauritius / Maurice", "Moldova", "Montserrat", "Moçambique", "México", "Namibia", "Naoero", "Nederland", "New Zealand / Aotearoa", "Nicaragua", "Niger", "Nigeria", "Niuē", "Norge", "Oʻzbekiston", "Panamá", "Papua Niugini", "Paraguay / Paraguái", "Perú", "Philippines", "Polska", "Portugal", "República Dominicana", "România", "Rwanda", "République démocratique du Congo", "Saint Helena, Ascension and Tristan da Cunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "San Marino", "Schweiz/Suisse/Svizzera/Svizra", "Sesel", "Shqipëria", "Sierra Leone", "Singapore", "Sint Maarten", "Slovenija", "Slovensko", "Solomon Islands", "Soomaaliland أرض الصومال", "Soomaaliya الصومال", "South Africa", "South Georgia and the South Sandwich Islands", "South Sudan", "Sri Lanka", "Suomi / Finland", "Suriname", "Sverige", "Sénégal", "Sāmoa", "Tanzania", "Tchad تشاد", "The Bahamas", "Timor-Leste", "Tonga", "Trinidad and Tobago", "Türkiye", "Türkmenistan", "Uganda", "United Kingdom", "United States", "Uruguay", "Venezuela", "Việt Nam", "Zambia", "Zimbabwe", "Éire / Ireland", "Ísland", "Österreich", "Česko", "Ελλάς", "Κύπρος - Kıbrıs", "Абхазия - Аԥсны", "Беларусь", "България", "Кыргызстан", "Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ", "Россия", "Северна Македонија", "Србија", "Тоҷикистон", "Україна", "Қазақстан", "Հայաստան", "ישראל", "افغانستان", "الأراضي الفلسطينية", "الأردن", "الإمارات العربية المتحدة", "البحرين", "السعودية", "السودان", "العراق", "الكويت", "اليمن", "ایران", "تونس", "سوريا", "عمان", "قطر", "لبنان", "مصر", "پاکستان", "ދިވެހިރާއްޖެ", "नेपाल", "বাংলাদেশ", "ประเทศไทย", "ປະເທດລາວ", "འབྲུག་ཡུལ།", "မြန်မာ", "საქართველო", "ኢትዮጵያ", "ព្រះរាជាណាចក្រ​កម្ពុជា", "Ṃajeḷ", "ⵍⵉⴱⵢⴰ ليبيا Libya", "ⵍⵣⵣⴰⵢⴻⵔ الجزائر", "中国", "日本", "臺灣", "대한민국", "조선민주주의인민공화국"];

  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function buildLabel(si, ci, ti, house) {
    return house + ' ' + STREETS[si] + ', ' + CITIES[ci] + ', ' + COUNTRIES[ti];
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var si = pickI(rnd, STREETS.length), ci = pickI(rnd, CITIES.length), ti = pickI(rnd, COUNTRIES.length);
    var house = 1 + Math.floor(rnd() * 9999);
    var n = (opts.baseN || 0) + 1;
    var pub = {
      id: ID_PREFIX + String(n).padStart(ID_DIGITS, '0'),
      n: n,
      kind: 'practice',
      street: STREETS[si],
      city: CITIES[ci],
      country: COUNTRIES[ti],
      house: String(house),
      label: buildLabel(si, ci, ti, house),
      note: NOTE,
      stamp: STAMP
    };
    pub._priv = { si: si, ci: ci, ti: ti, house: house, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'kind', 'street', 'city', 'country', 'house', 'label', 'note'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-ADDR-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.kind && rec.kind !== 'practice') errs.push('kind must be practice');
    if (typeof rec.note !== 'string' || rec.note.indexOf('NOT a verified real address') < 0)
      errs.push('practice disclaimer missing');
    if (rec._priv) {
      var p = rec._priv;
      var idxok = p.si >= 0 && p.si < STREETS.length && p.ci >= 0 && p.ci < CITIES.length &&
                  p.ti >= 0 && p.ti < COUNTRIES.length;
      if (!idxok) errs.push('private pool indices out of range');
      else {
        if (rec.street !== STREETS[p.si]) errs.push('street does not match private pick');
        if (rec.city !== CITIES[p.ci]) errs.push('city does not match private pick');
        if (rec.country !== COUNTRIES[p.ti]) errs.push('country does not match private pick');
        if (String(rec.house) !== String(p.house)) errs.push('house number does not match private pick');
        if (rec.label !== buildLabel(p.si, p.ci, p.ti, p.house)) errs.push('label does not rebuild from parts');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: a generated practice label must never equal a stored address label */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var lab = Array.isArray(a) ? a[1] : a.label;
      if (lab && String(lab) === String(rec.label))
        errs.push('label duplicates a stored archive address');
    });
    return { ok: errs.length === 0, errors: errs };
  }

  /* cross-database: borrow a theme number from another database's sample */
  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('earth', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: ['practice']
  });
})();
