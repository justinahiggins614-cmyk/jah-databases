/* JAH Chess and Board Games Database generator — jahdb-chess-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full game entry. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable chess/board-game facts) or Signature-generated
   (homegrown entries), labeled in `origin`. Never fabricates real-world facts. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'chess-games';
var PREFIX = 'JAH-CHS-';
var VERSION = 'jahdb-chess-games-1.0';
var RECORD_KIND = 'game entry';
var CATS = ['chess-opening', 'chess-strategy', 'board-game', 'game-rules'];

/* ================= REAL (sourced) data ================= */
/* Openings: [name, ECO, moves, description] */
var REAL_OPENINGS = [
['Ruy Lopez', 'C60\u2013C99', '1.e4 e5 2.Nf3 Nc6 3.Bb5', 'The Spanish Game: White pressures the knight defending e5. Named for the 16th-century Spanish priest Ruy L\u00f3pez de Segura. The richest and most deeply analyzed opening in chess.'],
['Italian Game', 'C50\u2013C59', '1.e4 e5 2.Nf3 Nc6 3.Bc4', 'The quiet game: rapid development toward the center and f7. Played for centuries; the Giuoco Piano (3...Bc5) is its classical heart.'],
['Sicilian Defense', 'B20\u2013B99', '1.e4 c5', 'Black\u2019s most popular and highest-scoring reply to 1.e4: an asymmetrical fight for the center with rich middlegame plans on both wings.'],
['French Defense', 'C00\u2013C19', '1.e4 e6', 'A solid counterattacking defense: Black builds a pawn chain and strikes at White\u2019s center with ...c5 and ...f6.'],
['Caro-Kann Defense', 'B10\u2013B19', '1.e4 c6', 'Black prepares ...d5 with solid pawn support; famously hard to break down and a favorite of positional players.'],
['Pirc Defense', 'B07\u2013B09', '1.e4 d6 2.d4 Nf6 3.Nc3 g6', 'A hypermodern defense: Black lets White build the center, then undermines it from the flank with ...Bg7.'],
['Scandinavian Defense', 'B01', '1.e4 d5', 'Black strikes at the center immediately with the queen\u2019s pawn; the modern 2...Qxd5 3.Nc3 Qa5 keeps the queen active.'],
['Alekhine\u2019s Defense', 'B02\u2013B05', '1.e4 Nf6', 'Black invites White\u2019s pawns forward with knight jumps, planning to undermine the overextended center.'],
['Queen\u2019s Gambit', 'D06\u2013D69', '1.d4 d5 2.c4', 'White offers the c-pawn to lure Black\u2019s center pawn away; declining or accepting shapes the whole middlegame.'],
['Queen\u2019s Gambit Declined', 'D30\u2013D69', '1.d4 d5 2.c4 e6', 'The classical QGD: Black holds the center with ...e6, leading to maneuvering battles and the famous minority attack.'],
['Queen\u2019s Gambit Accepted', 'D20\u2013D29', '1.d4 d5 2.c4 dxc4', 'Black grabs the gambit pawn and fights to hold it, accepting a slightly passive but tenacious position.'],
['Slav Defense', 'D10\u2013D19', '1.d4 d5 2.c4 c6', 'A rock-solid defense keeping the light-squared bishop\u2019s diagonal open; the Semi-Slav adds ...e6 for extra bite.'],
['King\u2019s Indian Defense', 'E60\u2013E99', '1.d4 Nf6 2.c4 g6', 'Black fianchettoes and prepares a kingside pawn storm; the most fighting defense to 1.d4, rich in opposite-wing attacks.'],
['Nimzo-Indian Defense', 'E20\u2013E59', '1.d4 Nf6 2.c4 e6 3.Nc3 Bb4', 'Black pins the knight to damage White\u2019s pawn structure; the strategic heavyweight of the 1.d4 complex.'],
['Queen\u2019s Indian Defense', 'E12\u2013E19', '1.d4 Nf6 2.c4 e6 3.Nf3 b6', 'A flexible fianchetto system: Black controls e4 from afar without committing the center pawns.'],
['Gr\u00fcnfeld Defense', 'D80\u2013D99', '1.d4 Nf6 2.c4 g6 3.Nc3 d5', 'Black lets White build a big center, then blasts it with ...d5 and ...c5; Kasparov\u2019s weapon of choice.'],
['English Opening', 'A10\u2013A39', '1.c4', 'A flank opening: White fights for d5 from the side, often transposing into favorable d4 systems with an extra tempo.'],
['R\u00e9ti Opening', 'A04\u2013A09', '1.Nf3', 'A hypermodern flank opening named for Richard R\u00e9ti, keeping central plans flexible while pressuring e5.'],
['London System', 'D02', '1.d4 d5 2.Bf4', 'White builds a solid pyramid with Bf4, e3, Nf3: easy to learn, hard to refute, and a modern online favorite.'],
['Dutch Defense', 'A80\u2013A99', '1.d4 f5', 'Black seizes kingside space immediately for an aggressive, unbalanced struggle; the Leningrad Dutch adds a fianchetto.'],
['Benoni Defense', 'A56\u2013A79', '1.d4 Nf6 2.c4 c5', 'Black accepts a queenside majority versus White\u2019s center; sharp, double-edged, and combative.'],
['King\u2019s Gambit', 'C30\u2013C39', '1.e4 e5 2.f4', 'The romantic gambit: White sacrifices the f-pawn for open lines and a kingside attack. The Immortal Game began this way.'],
['Evans Gambit', 'C51\u2013C52', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4', 'White offers the b-pawn for a tempo and a powerful center; a 19th-century swashbuckling favorite.'],
['Scotch Game', 'C44\u2013C45', '1.e4 e5 2.Nf3 Nc6 3.d4', 'White opens the center at once; Kasparov revived it in the 1990s with the sharp Mieses Variation.'],
['Four Knights Game', 'C48\u2013C49', '1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6', 'Symmetrical development; the Spanish Four Knights (4.Bb5) is the critical try for an edge.'],
['Petrov\u2019s Defense', 'C42\u2013C43', '1.e4 e5 2.Nf3 Nf6', 'The Russian Game: Black mirrors the knight attack, leading to symmetrical, solid positions.'],
['Vienna Game', 'C25\u2013C29', '1.e4 e5 2.Nc3', 'White delays Nf3 to keep f-pawn options; the Vienna Gambit (2...Nf6 3.f4) is its sharpest child.'],
['Danish Gambit', 'C21', '1.e4 e5 2.d4 exd4 3.c3', 'White sacrifices one or two pawns for a lead in development and open diagonals.'],
['Berlin Defense', 'C65\u2013C67', '1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6', 'The Berlin Wall: Kramnik used it to dethrone Kasparov in 2000 with a rock-solid endgame.'],
['Giuoco Piano', 'C50\u2013C54', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5', 'The quiet game\u2019s main line: both bishops aim at the center in a slow strategic duel.'],
['Two Knights Defense', 'C55\u2013C59', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6', 'Black counterattacks instead of defending; the Fried Liver Attack (4.Ng5) is White\u2019s wildest try.'],
['Scotch Gambit', 'C44', '1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4', 'A gambit hybrid of Scotch and Italian ideas with quick development.'],
['Philidor Defense', 'C41', '1.e4 e5 2.Nf3 d6', 'Fran\u00e7ois-Andr\u00e9 Philidor\u2019s solid defense: \u201cpawns are the soul of chess.\u201d'],
['Catalan Opening', 'E01\u2013E09', '1.d4 Nf6 2.c4 e6 3.g3', 'White fianchettoes for lasting queenside pressure; a positional squeeze rather than a knockout.'],
['Bogo-Indian Defense', 'E11', '1.d4 Nf6 2.c4 e6 3.Nf3 Bb4+', 'A quiet Nimzo cousin: Black develops smoothly and waits for White to overextend.'],
['Budapest Gambit', 'A51\u2013A52', '1.d4 Nf6 2.c4 e5', 'Black sacrifices a pawn for active piece play; a surprise weapon with real bite.'],
['Albin Countergambit', 'D08\u2013D09', '1.d4 d5 2.c4 e5', 'Black counter-sacrifices in the center and often wins the a-pawn trap line fame.'],
['Modern Defense', 'B06', '1.e4 g6', 'A hypermodern fianchetto defense keeping every central option open.'],
['King\u2019s Indian Attack', 'A07\u2013A08', '1.Nf3 d5 2.g3', 'A system, not a theory battle: White builds the same setup against almost anything.'],
['Colle System', 'D05', '1.d4 d5 2.Nf3 Nf6 3.e3', 'A solid pyramid aiming for the e5 break; beloved by club players for its clarity.'],
['Torre Attack', 'A46', '1.d4 Nf6 2.Nf3 e6 3.Bg5', 'Quick development with Bg5 pinning the knight; simple and surprisingly venomous.'],
['Trompowsky Attack', 'A45', '1.d4 Nf6 2.Bg5', 'White avoids main-line theory by developing the bishop aggressively on move two.'],
['Benko Gambit', 'A57\u2013A59', '1.d4 Nf6 2.c4 c5 3.d5 b5', 'Black sacrifices a pawn for lasting queenside pressure on open files; an endgame grinder\u2019s gambit.'],
['Smith-Morra Gambit', 'B21', '1.e4 c5 2.d4', 'White sacrifices a pawn against the Sicilian for open lines and a lead in development.'],
['Alapin Variation', 'B22', '1.e4 c5 2.c3', 'White sidesteps Sicilian theory with a solid pawn wedge, aiming for a strong center.'],
['Najdorf Variation', 'B90\u2013B99', 'Sicilian with 5...a6', 'Fischer\u2019s and Kasparov\u2019s Sicilian: flexible, aggressive, and the most analyzed variation in chess.'],
['Dragon Variation', 'B70\u2013B79', 'Sicilian with ...g6 and ...Bg7', 'Black fianchettoes into a razor-sharp opposite-side castling battle; the Yugoslav Attack is White\u2019s main try.'],
['Sveshnikov Variation', 'B33', '1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5', 'Black accepts a backward d-pawn for active piece play; a modern main line at the top level.'],
['Accelerated Dragon', 'B34\u2013B39', '1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6', 'The Dragon a tempo faster, avoiding the Yugoslav Attack but allowing the Maroczy Bind.'],
['Rossolimo Variation', 'B30\u2013B31', '1.e4 c5 2.Nf3 Nc6 3.Bb5', 'An anti-Sicilian: White avoids the open Sicilian\u2019s theory with a pinning bishop.'],
['Advance Variation (French)', 'C02', '1.e4 e6 2.d4 d5 3.e5', 'White grabs space; Black undermines with ...c5 and ...f6 in a tense strategic fight.'],
['Winawer Variation', 'C15\u2013C19', '1.e4 e6 2.d4 d5 3.Nc3 Bb4', 'Black pins and aims to shatter White\u2019s center; the sharpest French.'],
['Tarrasch Variation', 'C03\u2013C09', '1.e4 e6 2.d4 d5 3.Nd2', 'White avoids the Winawer pin and keeps the position flexible.'],
['Advance Variation (Caro-Kann)', 'B12', '1.e4 c6 2.d4 d5 3.e5', 'White takes space; Black plays ...Bf5 outside the chain and strikes with ...c5.'],
['Panov-Botvinnik Attack', 'B13\u2013B14', '1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4', 'White challenges the Caro structure directly, often reaching isolated-queen-pawn positions.'],
['Marshall Attack', 'C89', 'Ruy Lopez with 8...d5', 'Black sacrifices a pawn for a raging initiative; one of the most analyzed gambits ever.'],
['Exchange Ruy Lopez', 'C68', '1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6', 'White damages Black\u2019s structure and heads for a better endgame; Fischer\u2019s choice in 1992.'],
['Fried Liver Attack', 'C57', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.Nxf7', 'White sacrifices the knight on f7 for a ferocious attack; club players\u2019 favorite fireworks.'],
['Traxler Counterattack', 'C57', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 Bc5', 'Black ignores the f7 threat and counterattacks; gloriously chaotic.'],
['Halloween Gambit', 'C47', '1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Nxe5', 'White sacrifices the knight for a pawn roller of center pawns; scary and sound-ish.'],
['Belgrade Gambit', 'C47', '1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.d4', 'An aggressive Four Knights gambit with quick central pressure.'],
['Latvian Gambit', 'C40', '1.e4 e5 2.Nf3 f5', 'Black gambits the f-pawn for mayhem; dubious but dangerous over the board.'],
['Elephant Gambit', 'C40', '1.e4 e5 2.Nf3 d5', 'Black throws the d-pawn forward for open, chaotic play.'],
['Hungarian Defense', 'C50', '1.e4 e5 2.Nf3 Nc6 3.Bc4 Be7', 'A quiet, solid alternative to 3...Bc5 or ...Nf6.'],
['Bishop\u2019s Opening', 'C23\u2013C24', '1.e4 e5 2.Bc4', 'An old romantic opening, flexible and transpositional.'],
['Ponziani Opening', 'C44', '1.e4 e5 2.Nf3 Nc6 3.c3', 'White builds a big center with c3 and d4; an ancient opening with modern bite.'],
['G\u00f6ring Gambit', 'C44', 'Scotch with 4.c3', 'White offers a pawn for a massive center and development.'],
['Chigorin Defense', 'D07', '1.d4 d5 2.c4 Nc6', 'Black develops the knight provocatively; Morozevich\u2019s surprise weapon.'],
['Semi-Slav Defense', 'D43\u2013D49', '1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 e6', 'The ambitious Slav: Black keeps the bishop in but risks the center tension.'],
['Stonewall Attack', 'D00', '1.d4 d5 2.e3', 'White builds a stonewall pawn formation for a kingside attack; simple plans, real punch.'],
['Blackmar-Diemer Gambit', 'D00', '1.d4 d5 2.e4', 'White sacrifices for open lines; the club gambiteer\u2019s delight.'],
['Veresov Opening', 'D01', '1.d4 d5 2.Nc3 Nf6 3.Bg5', 'Quick development with early pressure; an anti-theory choice.'],
['Jobava London', 'D00', '1.d4 d5 2.Nc3 Nf6 3.Bf4', 'The aggressive London: Nc3 supports e4 breaks and kingside storms.'],
['Bird\u2019s Opening', 'A02\u2013A03', '1.f4', 'White seizes kingside space at the cost of king safety; From\u2019s Gambit (1...e5) is the critical test.'],
['Sokolsky Opening', 'A00', '1.b4', 'The Polish Opening: White fianchettoes from the flank and fights for the center sideways.'],
['Larsen\u2019s Opening', 'A01', '1.b3', 'Bent Larsen\u2019s hypermodern flank opening with an early fianchetto.'],
['Grob\u2019s Attack', 'A00', '1.g4', 'The most provocative first move: weakening but full of traps.'],
['Van Geet Opening', 'A00', '1.Nc3', 'An offbeat developing move keeping all options open.'],
['King\u2019s Fianchetto Opening', 'B06', '1.g3', 'White fianchettoes immediately for a flexible hypermodern setup.'],
['Nimzowitsch Defense', 'B00', '1.e4 Nc6', 'Black develops the knight provocatively, aiming for ...d5 or ...e5 breaks.'],
['Owen\u2019s Defense', 'B00', '1.e4 b6', 'A fianchetto defense against 1.e4; solid but slightly passive.'],
['St. George Defense', 'B00', '1.e4 a6', 'The provocative ...a6 and ...b5 plan; famously used by Tony Miles to beat Karpov in 1980.'],
['Englund Gambit', 'A40', '1.d4 e5', 'Black sacrifices for quick development; tricky in blitz.'],
['Blumenfeld Countergambit', 'E10', '1.d4 Nf6 2.c4 e6 3.Nf3 c5 4.d5 b5', 'Black sacrifices a wing pawn for central pressure; a Benko-like idea in the Bogo complex.'],
['Mieses Opening', 'A00', '1.d3', 'A quiet, flexible first move avoiding all theory.'],
['Anderssen\u2019s Opening', 'A00', '1.a3', 'A waiting move named for Adolf Anderssen; harmless but playable.'],
['Clemenz Opening', 'A00', '1.h3', 'A prophylactic edge move; the slowest of starts.'],
['Saragossa Opening', 'A00', '1.c3', 'A solid, modest first move supporting d4.'],
['Ware Opening', 'A00', '1.a4', 'The Meadow Hay Opening: an offbeat flank push.'],
['Van\u2019t Kruijs Opening', 'A00', '1.e3', 'A quiet developing move, fully playable if unambitious.']
];

/* Strategy: [title, topic, description] */
var REAL_STRATEGY = [
['Piece values', 'evaluation', 'The standard scale: pawn 1, knight and bishop 3 each, rook 5, queen 9. The bishop pair and piece activity adjust these numbers in real positions.'],
['Control the center', 'opening principle', 'Occupy or influence e4, d4, e5, d5 with pawns and pieces; central control gives mobility and attacking chances on both wings.'],
['Develop with threats', 'opening principle', 'Bring knights and bishops out toward the center, preferably with tempo \u2014 attacking something while developing.'],
['Castle early', 'opening principle', 'King safety first: castle within the first ten moves in most openings before launching operations.'],
['Don\u2019t move the same piece twice', 'opening principle', 'In the opening, finish development before moving developed pieces again \u2014 every tempo counts.'],
['The fork', 'tactics', 'One piece attacks two or more enemy pieces at once; knight forks are the most famous and feared.'],
['The pin', 'tactics', 'A piece cannot move without exposing a more valuable piece behind it; absolute pins (against the king) freeze the piece entirely.'],
['The skewer', 'tactics', 'The reverse pin: attack a valuable piece so it must move, winning the piece behind it.'],
['Discovered attack', 'tactics', 'Move one piece away to unleash a line piece\u2019s attack \u2014 often with check for maximum force.'],
['Double check', 'tactics', 'Two pieces check the king at once; the king must move, since neither check can be blocked or captured.'],
['Deflection', 'tactics', 'Lure a defending piece away from its duty with a sacrifice or threat.'],
['The decoy', 'tactics', 'Force an enemy piece onto a bad square where it can be attacked or trapped.'],
['Back-rank mate', 'checkmate pattern', 'A rook or queen delivers mate on the opponent\u2019s back rank when their own pawns block the king\u2019s escape.'],
['Scholar\u2019s mate', 'checkmate pattern', '1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6 4.Qxf7#: the four-move mate every beginner learns \u2014 and learns to stop.'],
['Fool\u2019s mate', 'checkmate pattern', '1.f3 e5 2.g4 Qh4#: the fastest possible checkmate, in two moves.'],
['Smothered mate', 'checkmate pattern', 'A knight mates a king completely surrounded by its own pieces \u2014 Philidor\u2019s legacy.'],
['Anastasia\u2019s mate', 'checkmate pattern', 'Knight and rook combine: the knight covers escape squares while the rook mates on the h-file.'],
['Arabian mate', 'checkmate pattern', 'Knight and rook mate a cornered king: one of the oldest known patterns.'],
['Boden\u2019s mate', 'checkmate pattern', 'Two bishops on crossing diagonals mate a king trapped by its own pieces.'],
['King and queen vs king', 'endgame', 'Drive the lone king to the edge with the queen, then mate with king support; the queen must avoid stalemate.'],
['King and rook vs king', 'endgame', 'Cut off ranks with the rook, bring the king up, and mate on the edge \u2014 the box method.'],
['The opposition', 'endgame', 'Kings facing each other with one square between: the side not to move has the opposition and wins the key squares.'],
['The Lucena position', 'endgame', 'The winning method for rook and pawn vs rook: build the bridge to shelter the king from checks.'],
['The Philidor position', 'endgame', 'The drawing method for rook and pawn vs rook: keep the rook on the sixth rank cutting off the king.'],
['Pawn promotion', 'endgame', 'A pawn reaching the last rank promotes, usually to a queen; underpromotion to knight can avoid stalemate or fork.'],
['Triangulation', 'endgame', 'Lose a tempo with king triangulation to put the opponent in zugzwang.'],
['En passant', 'rules', 'A pawn moving two squares beside an enemy pawn can be captured as if it had moved one \u2014 only on the very next move.'],
['Castling rules', 'rules', 'Castle only if king and rook are unmoved, no pieces between, the king is not in check and does not pass through check.'],
['Touch-move', 'rules', 'If you deliberately touch a piece, you must move it if legal \u2014 \u201cj\u2019adoube\u201d (I adjust) excepts.'],
['Fifty-move rule', 'rules', 'A draw can be claimed if fifty moves pass with no pawn move and no capture.'],
['Threefold repetition', 'rules', 'A draw can be claimed when the same position occurs three times with the same side to move.'],
['Insufficient material', 'rules', 'King vs king, king+minor piece vs king, and king+bishop vs king+bishop (same color) are automatic draws.'],
['Stalemate', 'rules', 'No legal moves and not in check is stalemate \u2014 an immediate draw, and a constant swindling resource.'],
['The exchange sacrifice', 'strategy', 'Giving rook for minor piece for positional compensation: initiative, pawn structure, or king safety.'],
['Prophylaxis', 'strategy', 'Prevent the opponent\u2019s plans before executing your own \u2014 the hallmark of Karpov and Carlsen.'],
['The minority attack', 'strategy', 'Advance a pawn minority to inflict a backward pawn or weak square on the majority \u2014 the QGD\u2019s signature plan.'],
['Outposts', 'strategy', 'A knight planted on a square no enemy pawn can attack, deep in enemy territory, can dominate a game.'],
['Open files for rooks', 'strategy', 'Rooks belong on open files; doubled rooks on the seventh rank are worth a pawn.'],
['Bishop pair', 'strategy', 'Two bishops against bishop+knight is a lasting edge in open positions, worth roughly half a pawn.'],
['Space advantage', 'strategy', 'More space means more maneuvering room; cramp the opponent, then strike where they are weakest.'],
['The initiative', 'strategy', 'Keep making threats so the opponent must respond; the initiative can outweigh material.']
];
/* Board games: [name, players, year, designer, description] */
var REAL_GAMES = [
['Chess', '2', '', '', 'The royal game: ancient strategy of perfect information, descended from Indian chaturanga (~6th century). The world\u2019s most studied board game.'],
['Go', '2', '', '', 'The ancient Chinese game of surrounding territory with stones on a 19x19 grid; simple rules, profound depth.'],
['Checkers (Draughts)', '2', '', '', 'Jump and capture across the board; kings fly in international draughts. A folk classic on every continent.'],
['Backgammon', '2', '', '', 'One of the oldest known board games: race and capture around the board with dice and strategy.'],
['Mahjong', '4', '', '', 'The Chinese tile game of sets and pairs, blending luck, memory, and tactics.'],
['Dominoes', '2\u20134', '', '', 'Match pips end to end; the double-six set holds 28 tiles of pure combinatorial folk play.'],
['Scrabble', '2\u20134', '1938', 'Alfred Butts', 'The crossword game: build interlocking words for points on premium squares.'],
['Monopoly', '2\u20138', '1935', 'Parker Brothers', 'Buy, trade, and bankrupt: the property-trading classic that has ended friendships since the Depression.'],
['Risk', '2\u20136', '1957', 'Albert Lamorisse', 'World conquest by dice and diplomacy; the gateway game of global domination.'],
['Clue (Cluedo)', '3\u20136', '1949', 'Anthony Pratt', 'Deduction in the mansion: who, with what, in which room?'],
['Battleship', '2', '1967', 'Milton Bradley', 'Hidden fleets and called coordinates: \u201cYou sank my battleship!\u201d'],
['Stratego', '2', '1961', 'Milton Bradley', 'Hidden ranks and the flag: memory and bluffing on the battlefield.'],
['Diplomacy', '7', '1959', 'Allan B. Calhamer', 'Pure negotiation: no dice, no luck \u2014 only promises, and breaking them.'],
['Acquire', '2\u20136', '1964', 'Sid Sackson', 'Found hotel chains, merge them, and get rich: the stock-market board game.'],
['The Game of Life', '2\u20136', '1960', 'Milton Bradley', 'Spin through careers, family, and retirement on the winding road.'],
['Candy Land', '2\u20134', '1949', 'Eleanor Abbott', 'The first-race classic for young children: draw a card, move to the color.'],
['Sorry!', '2\u20134', '1934', 'Parker Brothers', 'Send rivals home in this cross-and-circle race with a grudge.'],
['Yahtzee', '1+', '1956', '', 'Five dice, thirteen categories: the yachtzee is fifty points of glory.'],
['Trivial Pursuit', '2\u20136', '1981', 'Chris Haney & Scott Abbott', 'Six wedges of trivia across the wheel: the 1980s phenomenon.'],
['Pictionary', '4+', '1985', '', 'Draw the word before the sand runs out; artistry optional, shouting encouraged.'],
['Catan', '3\u20134', '1995', 'Klaus Teuber', 'Settle the island: trade wood, brick, sheep, wheat, and ore to ten victory points. The modern hobby\u2019s big bang.'],
['Carcassonne', '2\u20135', '2000', 'Klaus-J\u00fcrgen Wrede', 'Tile-laying medieval France: claim roads, cities, and fields with your meeples.'],
['Ticket to Ride', '2\u20135', '2004', 'Alan R. Moon', 'Claim rail routes across the map; the friendliest gateway game ever made.'],
['Pandemic', '2\u20134', '2008', 'Matt Leacock', 'Cooperate to cure four diseases before the outbreaks cascade: the definitive co-op.'],
['Dominion', '2\u20134', '2008', 'Donald X. Vaccarino', 'The deck-builder: buy cards to build an engine from ten kingdom piles.'],
['7 Wonders', '3\u20137', '2010', 'Antoine Bauza', 'Draft cards through three ages and raise a wonder; simultaneous play, zero downtime.'],
['Splendor', '2\u20134', '2014', 'Marc Andr\u00e9', 'Collect gems, buy developments, attract nobles: engine-building in thirty minutes.'],
['Azul', '2\u20134', '2017', 'Michael Kiesling', 'Tile the palace walls of \u00c9vora; beautiful, brutal, and tactile.'],
['Codenames', '4+', '2015', 'Vlaada Chv\u00e1til', 'One-word clues link your team\u2019s secret words \u2014 avoid the assassin.'],
['Power Grid', '2\u20136', '2004', 'Friedemann Friese', 'Bid on power plants, buy fuel, and light cities: the economist\u2019s auction game.'],
['Puerto Rico', '3\u20135', '2002', 'Andreas Seyfarth', 'Role selection on the colonial island: ship goods, build, and prosper.'],
['Agricola', '1\u20135', '2007', 'Uwe Rosenberg', 'Feed your family from a struggling farm: the worker-placement classic.'],
['Gloomhaven', '1\u20134', '2017', 'Isaac Childres', 'A campaign of tactical card combat in a persistent fantasy world; the hobby\u2019s heavyweight.'],
['Wingspan', '1\u20135', '2019', 'Elizabeth Hargrave', 'Attract birds to your wildlife preserves in this serene engine-builder.'],
['Chess960', '2', '1996', 'Bobby Fischer', 'Fischer Random: the back rank is shuffled among 960 positions to kill opening theory.'],
['Shogi', '2', '', '', 'Japanese chess: captured pieces change sides and drop back into play.'],
['Xiangqi', '2', '', '', 'Chinese chess: cannons leap, generals guard the palace, played on points not squares.'],
['Janggi', '2', '', '', 'Korean chess: no castling, elephants instead of bishops, a game of maneuver.'],
['Othello', '2', '1971', '', 'A minute to learn, a lifetime to master: outflank rows of discs on the 8x8 board.'],
['Connect Four', '2', '1974', 'Milton Bradley', 'Drop checkers, connect four: the vertical tic-tac-toe.'],
['Mastermind', '2', '1970', '', 'Crack the color code in ten guesses of logic.'],
['Jenga', '1+', '1983', 'Leslie Scott', 'Pull blocks, stack high, defy gravity until the tower falls.'],
['Uno', '2\u201310', '1971', 'Merle Robbins', 'Match color or number; shout UNO at one card left.'],
['Boggle', '1+', '1972', '', 'Shake sixteen letter dice and find words in three minutes.'],
['Hive', '2', '2000', 'John Yianni', 'The bug chess: surround the enemy queen bee with your crawling tiles \u2014 no board needed.'],
['Patchwork', '2', '2014', 'Uwe Rosenberg', 'Sew a quilt from Tetris tiles; the coziest two-player duel.'],
['Jaipur', '2', '2009', 'S\u00e9bastien Pauchon', 'Trade goods in the Indian market; fast, sharp, and replayable.'],
['Lost Cities', '2', '1999', 'Reiner Knizia', 'Launch expeditions with numbered cards; press your luck across five colors.'],
['Tigris & Euphrates', '2\u20134', '1997', 'Reiner Knizia', 'Build Mesopotamian kingdoms in four colors; Knizia\u2019s masterpiece of conflict.'],
['Modern Art', '3\u20135', '1992', 'Reiner Knizia', 'Auction paintings whose value is set by the market you create.'],
['Ra', '2\u20135', '1999', 'Reiner Knizia', 'Bid on Egyptian lots before Ra\u2019s barge arrives; auction tension perfected.'],
['El Grande', '2\u20135', '1995', '', 'Area majority in Renaissance Spain with the caballero and the castillo.'],
['Alhambra', '2\u20136', '2003', '', 'Build the palace complex with currency in four colors.'],
['Stone Age', '2\u20134', '2008', '', 'Worker placement in the Stone Age: feed your tribe and build huts.'],
['Small World', '2\u20135', '2009', '', 'Fantasy races conquer and decline across a too-small map.'],
['King of Tokyo', '2\u20136', '2011', 'Richard Garfield', 'Giant monsters punch each other for Tokyo; Yahtzee with claws.'],
['Love Letter', '2\u20134', '2012', 'Seiji Kanai', 'Sixteen cards, one princess: deduction in a single hand.'],
['Sushi Go!', '2\u20135', '2013', '', 'Draft the tastiest sushi combo; pudding lovers beware.'],
['The Resistance', '5\u201310', '2009', '', 'Hidden spies sabotage missions; social deduction at its purest.'],
['Avalon', '5\u201310', '2012', '', 'Resistance with Merlin and the Assassin: deduction with special roles.'],
['Werewolf', '7+', '1986', 'Dimitry Davidoff', 'Villagers hunt hidden werewolves through day debate and night kills.'],
['Dixit', '3\u20136', '2008', 'Jean-Louis Roubira', 'Give a clue for your dreamlike illustration; guessers score the poetry.'],
['Mysterium', '2\u20137', '2013', '', 'A ghost sends vision cards to mediums to solve its murder: co-op Dixit with a killer.'],
['Betrayal at House on the Hill', '3\u20136', '2004', '', 'Explore the haunted house until the haunt begins \u2014 then someone turns traitor.'],
['Twilight Imperium', '3\u20138', '1997', '', 'The epic of galactic conquest: eight hours of diplomacy, war, and politics.'],
['Scythe', '1\u20135', '2016', 'Jamey Stegmaier', 'Alternate-1920s Europa: mechs, workers, and engine-building efficiency.'],
['Terraforming Mars', '1\u20135', '2016', 'Jacob Fryxelius', 'Raise the temperature, oxygen, and oceans of Mars with two hundred project cards.'],
['Brass: Birmingham', '2\u20134', '2007', 'Martin Wallace', 'Build the Industrial Revolution\u2019s canal and rail networks.'],
['Spirit Island', '1\u20134', '2017', '', 'Cooperative anti-colonial defense: spirits drive invaders from the island.'],
['Root', '2\u20134', '2018', 'Cole Wehrle', 'Asymmetric woodland warfare: each faction plays a different game.'],
['Everdell', '1\u20134', '2018', '', 'Build a woodland city of critters and constructions under the great tree.'],
['Cascadia', '1\u20134', '2021', '', 'Tile-laying Pacific Northwest habitats and wildlife corridors.'],
['Ark Nova', '1\u20134', '2021', 'Mathias Wigge', 'Build a modern zoo for conservation and appeal; the heavyweight of 2021.'],
['Dune: Imperium', '1\u20134', '2020', '', 'Deck-building meets worker placement on Arrakis; the spice must flow.'],
['Lost Ruins of Arnak', '1\u20134', '2020', '', 'Explore jungle ruins with deck-building and worker placement.'],
['Twilight Struggle', '2', '2005', 'Ananda Gupta & Jason Matthews', 'The Cold War in cards: influence, coups, and DEFCON tension.'],
['Star Realms', '2', '2014', '', 'Deck-building space combat in twenty minutes.'],
['Clank!', '2\u20134', '2016', '', 'Deck-building dungeon heist: grab the artifact and escape the dragon quietly.'],
['Quacks of Quedlinburg', '2\u20134', '2018', '', 'Push-your-luck potion brewing: draw ingredients until the cauldron explodes.'],
['The Crew', '2\u20135', '2019', '', 'Cooperative trick-taking in space: fifty missions of silent teamwork.'],
['The Mind', '2\u20134', '2018', '', 'Play cards in ascending order without talking: telepathy as a game.'],
['Hanabi', '2\u20135', '2010', 'Antoine Bauza', 'Cooperative fireworks: you see everyone\u2019s cards but your own.'],
['Wavelength', '2\u201312', '2019', '', 'The telepathy party game: where on the spectrum is the target?'],
['Just One', '3\u20137', '2018', '', 'Cooperative word guessing with duplicate clues canceled.'],
['Decrypto', '3\u20138', '2018', '', 'Teams encrypt words for teammates while intercepting the enemy\u2019s codes.'],
['Coup', '2\u20136', '2012', 'Rikki Tahta', 'Bluffing dystopia: claim roles, call lies, launch coups.'],
['Skull', '3\u20136', '2011', 'Herv\u00e9 Marly', 'Bid on how many coasters you can flip without hitting a skull.'],
['Cockroach Poker', '2\u20136', '2004', 'Jacques Zeimet', 'Bluff critters onto rivals; no turns, just nerve.'],
['6 Nimmt!', '2\u201310', '1994', 'Wolfgang Kramer', 'Take the sixth card in a row and eat the bullheads.'],
['No Thanks!', '3\u20137', '2004', 'Thorsten Gimmler', 'Take the card or pay a chip: the purest auction filler.'],
['For Sale', '3\u20136', '1997', 'Stefan Dorra', 'Buy low, sell high: two-phase property flipping in twenty minutes.'],
['Coloretto', '3\u20135', '2003', 'Michael Schacht', 'Take the row or add to it: set collection with delicious pain.'],
['Twister', '2+', '1966', 'Milton Bradley', 'Right hand red: the mat-twisting party classic.'],
['Exploding Kittens', '2\u20135', '2015', '', 'Russian roulette with cards and a record-breaking crowdfunding campaign.'],
['Blood on the Clocktower', '7+', '2022', '', 'Social deduction with no player elimination: the storyteller runs the demon hunt.'],
['One Night Ultimate Werewolf', '3\u201310', '2014', 'Ted Alspach & Akihisa Okui', 'Ten minutes, one night, shifting roles: werewolf at speed.'],
['Frosthaven', '1\u20134', '2022', 'Isaac Childres', 'Gloomhaven\u2019s arctic successor: campaign tactics in the frozen north.'],
['Sleeping Gods', '1\u20134', '2021', '', 'Atlas-game exploration across a mythic sea in a storybook campaign.'],
['Nemesis', '1\u20135', '2018', '', 'Sci-fi survival horror aboard a dead ship; trust no one.'],
['Zombicide', '1\u20136', '2012', '', 'Cooperative zombie survival with mountains of miniatures.'],
['Dead of Winter', '2\u20135', '2014', '', 'Survive the winter colony \u2014 but someone may be the betrayer.'],
['Robinson Crusoe', '1\u20134', '2012', 'Ignacy Trzewiczek', 'Cooperative castaway survival through brutal scenario campaigns.'],
['This War of Mine', '1\u20136', '2017', '', 'Civilians surviving a siege: the board game of moral weight.'],
['Mage Knight', '1\u20134', '2011', 'Vlaada Chv\u00e1til', 'The epic of deck-building conquest across the Atlantean Empire.'],
['Too Many Bones', '1\u20134', '2017', '', 'Dice-building RPG boss battles with the Gearlocs.'],
['Oath', '1\u20136', '2021', 'Cole Wehrle', 'A legacy game of empire where each session rewrites the chronicle.'],
['Pax Pamir', '1\u20135', '2015', 'Cole Wehrle', 'The Great Game in Afghanistan: tableau-building imperial intrigue.'],
['John Company', '1\u20136', '2017', 'Cole Wehrle', 'Negotiate the East India Company\u2019s fortunes \u2014 and its crimes.'],
['1830', '2\u20137', '1986', 'Francis Tresham', 'The railway stock game that founded the 18xx genre.'],
['Hannibal: Rome vs. Carthage', '2', '1996', '', 'Card-driven Second Punic War: elephants over the Alps.'],
['Paths of Glory', '2', '1999', '', 'The First World War as a card-driven struggle of trenches.'],
['Star Wars: Rebellion', '2\u20134', '2016', '', 'The Galactic Civil War: hidden base, Death Star, and epic asymmetry.'],
['War of the Ring', '2\u20134', '2004', '', 'The Lord of the Rings as grand strategy: the Fellowship vs the Shadow.'],
['Axis & Allies', '2\u20135', '1981', '', 'The Second World War in a box: the classic hex-and-counter epic.'],
['Hero Realms', '2\u20134', '2016', '', 'Fantasy deck-building duels in the Star Realms engine.'],
['Ascension', '2\u20134', '2010', '', 'Deck-building with a center row of heroes, monsters, and constructs.'],
['Aeon\u2019s End', '1\u20134', '2016', '', 'Cooperative deck-building against the Nameless: never shuffle your discard.'],
['Marvel Legendary', '1\u20135', '2012', '', 'Deck-building heroics against Marvel masterminds.'],
['Eldritch Horror', '1\u20138', '2013', '', 'Cooperative globe-trotting against the Ancient Ones.'],
['Mansions of Madness', '1\u20135', '2011', '', 'App-driven Lovecraftian investigation in the haunted mansion.'],
['Arkham Horror (3rd ed.)', '1\u20136', '2005', '', 'Cooperative occult investigation across 1920s Arkham.'],
['Descent', '2\u20135', '2005', '', 'Dungeon-crawl campaign: heroes vs the overlord.'],
['Eclipse', '2\u20136', '2011', '', '4X space empire in two hours: explore, expand, exploit, exterminate.'],
['Through the Ages', '2\u20134', '2006', 'Vlaada Chv\u00e1til', 'Civilization in cards: the heavyweight civ-builder without a map.'],
['Great Western Trail', '2\u20134', '2016', 'Alexander Pfister', 'Drive cattle to Kansas City in this rondel of deck-building and buildings.'],
['Food Chain Magnate', '2\u20135', '2015', '', 'Ruthless fast-food empire building: the heavyweight business sim.'],
['Terra Mystica', '2\u20135', '2012', 'Helge Ostertag & Jens Dr\u00f6gem\u00fcller', 'Terraform the map for your fantasy faction\u2019s needs.'],
['Gaia Project', '1\u20134', '2017', '', 'Terra Mystica in space: the refined sequel among the stars.'],
['Project L', '1\u20134', '2020', '', 'Tetris-like polyomino puzzles with an engine-building twist.'],
['Kingdomino', '2\u20134', '2016', '', 'Domino kingdoms: draft tiles, build 5x5, crown the best realm.'],
['King of Tokyo: Dark Edition', '2\u20136', '2020', '', 'The monster duel, reforged with wicked powers.'],
['The Quacks of Quedlinburg: The Alchemists', '2\u20134', '2020', '', 'The hit potion-brewer\u2019s expansion of essences.'],
['Parks', '1\u20135', '2019', '', 'Hike the US national parks in this serene trail-builder.'],
['Tokaido', '2\u20135', '2012', 'Antoine Bauza', 'Stroll the East Sea Road collecting the journey\u2019s most beautiful moments.'],
['Takenoko', '2\u20134', '2011', 'Antoine Bauza', 'Grow bamboo for the Emperor\u2019s panda in this charming garden game.'],
['Ramen Fury', '2\u20135', '2019', '', 'Slurp up ingredient cards to complete the tastiest bowls.'],
['Point Salad', '2\u20136', '2019', '', 'Draft veggies and scoring cards: 15 minutes of crisp decisions.'],
['The Fox in the Forest', '2', '2017', '', 'Trick-taking fairy tale for two: win tricks, but not too many.'],
['Schotten Totten', '2', '1999', 'Reiner Knizia', 'Claim the stones with poker-like formations: tug-of-war perfected.'],
['Battle Line', '2', '2000', 'Reiner Knizia', 'The rethemed Schotten Totten: flags and formations.'],
['Air, Land & Sea', '2', '2019', '', 'Eighteen cards, three theaters, endless bluffing.'],
['Radlands', '2', '2021', '', 'Post-apocalyptic water wars with punk-art punch.'],
['Mindbug', '2', '2021', '', 'Creature duels where you can steal the opponent\u2019s best plays.'],
['Star Wars: The Deckbuilding Game', '2', '2023', '', 'Rebels vs Empire in the deck-building duel.'],
['Heat: Pedal to the Metal', '1\u20136', '2022', '', 'Race-car push-your-luck around the track\u2019s corners.'],
['Flamecraft', '1\u20135', '2022', '', 'Cozy artisan dragons in a charming town-builder.'],
['My City', '2\u20134', '2020', 'Reiner Knizia', 'Legacy polyomino city-building across 24 evolving episodes.'],
['Cartographers', '1\u2013100', '2019', '', 'Flip-and-write mapmaking for the queen\u2019s surveyors.'],
['Welcome To...', '1\u2013100', '2018', '', 'Build 1950s suburbia in this flip-and-write classic.'],
['Railroad Ink', '1\u20136', '2018', '', 'Roll dice, draw routes, connect the network.'],
['Ganz Sch\u00f6n Clever', '1\u20134', '2018', '', 'Roll-and-write dice optimization at its cleverest.'],
['Troyes Dice', '1\u201310', '2020', '', 'The dice version of the medieval city-builder.'],
['Hadrian\u2019s Wall', '1\u20136', '2021', '', 'Flip-and-write Roman frontier defense with combo-tastic sheets.'],
['Dune: Imperium \u2013 Uprising', '1\u20136', '2023', '', 'The standalone sequel refining Arrakis deck-building.'],
['Sky Team', '2', '2023', '', 'Cooperative dice-placement landing of an airliner; silent teamwork.'],
['Forest Shuffle', '2\u20135', '2023', '', 'Build the best forest ecosystem from woodland cards.'],
['Harmonies', '1\u20134', '2024', '', 'Build landscapes for animals in 3D spatial puzzling.']
];
/* Rules: [title, description] */
var REAL_RULES = [
['How chess moves: the pieces', 'King one square any direction; queen any distance orthogonally or diagonally; rooks straight; bishops diagonal; knights in L jumps; pawns forward one (two from start), capturing diagonally.'],
['Check, checkmate, stalemate', 'Check attacks the king and must be answered; checkmate ends the game; stalemate (no legal move, not in check) is a draw.'],
['Chess notation', 'Algebraic notation names every square (e4, Nf3); + is check, # is mate, O-O castles kingside, ! and ? annotate quality.'],
['The chess clock', 'Each player\u2019s time runs only on their move; flagging (time out) loses unless the opponent cannot possibly mate.'],
['Tournament formats', 'Round-robin (everyone plays everyone) and Swiss system (paired by score each round) are the standard formats.'],
['How Go is played', 'Players alternate placing stones on intersections; surrounded stones and territory are captured; the player with more territory wins.'],
['How checkers is played', 'Men move diagonally forward and jump to capture; reaching the far rank crowns a king that moves both ways.'],
['How backgammon is played', 'Race fifteen checkers around the board by dice rolls; blots can be hit and must re-enter.'],
['How Scrabble scoring works', 'Letters carry point values; premium squares double or triple letter and word scores; all seven tiles at once earns a 50-point bingo.'],
['How Monopoly is played', 'Roll, move, buy properties, build houses and hotels, and bankrupt rivals; jail, Chance, and Community Chest add chaos.'],
['How Risk is played', 'Draft armies, attack adjacent territories with dice, and hold continents for bonuses until one player rules the map.'],
['How Catan is played', 'Roll for resources, trade, build roads and settlements, and reach ten victory points; the robber punishes the leader.'],
['How Uno is played', 'Match the top card by color, number, or symbol; action cards skip, reverse, and draw; going out wins the round.'],
['How Ticket to Ride is played', 'Collect colored train cards to claim routes; complete destination tickets for points, lose them if you fail.'],
['How Pandemic is played', 'On your turn take four actions (move, treat, cure, build), then draw infections; cure all four diseases to win together.'],
['How chess960 setup works', 'The back rank is randomized among 960 legal positions with bishops on opposite colors; castling rules adapt to the setup.'],
['The 50-move and repetition draws', 'Either player may claim a draw after fifty moveless moves or threefold repetition of position.'],
['FIDE laws: illegal moves', 'An illegal move in standard play loses the game if the opponent claims before moving (with clock-press rules varying by time control).'],
['Handicaps in Go', 'Weaker players take extra black stones placed on star points; the handicap scale runs from 2 to 9 stones.'],
['Shogi drops', 'Captured pieces switch sides and may be dropped on empty squares instead of moving \u2014 the heart of Japanese chess.']
];

/* ================= Signature-generation pools ================= */
var REP_TOPICS = [
['Building a 1.e4 repertoire for club players','chess-opening','Choose one defense to 1.e4, one to 1.d4, and learn the resulting middlegame plans rather than memorizing twenty moves deep.','Pick your weapons: one reliable answer to 1.e4 (Caro-Kann or French for solidity, Sicilian for fight), one to 1.d4 (Slav or Nimzo-Indian). Study the pawn structures: learn the three pawn breaks and two piece maneuvers that define each. Play practice games: test the repertoire online at longer time controls and log where you felt lost. Patch the holes: after each loss, learn exactly one new line \u2014 depth follows need.'],
['Building a 1.d4 repertoire for club players','chess-opening','A compact, solid repertoire: London System or Catalan ideas as White; King\u2019s Indian or Nimzo/QGD complex as Black.','Choose your system: the London for low-theory solidity or the Catalan for lasting pressure. Learn the structures: the hanging pawns, the isolated queen pawn, and the minority attack define d4 middlegames. Drill the tactics: d4 positions punish slow development, so solve ten tactics daily. Review monthly: one repertoire review session beats ten random videos.'],
['Surviving the Sicilian as White','chess-opening','Anti-Sicilians (Alapin, Rossolimo, Closed) dodge the theory jungle while keeping real chances.','Pick your anti: 2.c3 for solidity, 3.Bb5 for pressure, or the Closed for slow squeezes. Learn the plans: each anti has one central idea \u2014 master it. Punish overconfidence: Sicilian players crave open chaos; keep it positional. Practice the structures: play training games from move 8 of your chosen line.'],
['Handling the French Winawer','chess-opening','The Winawer\u2019s poisoned-pawn chaos rewards the prepared and punishes the casual.','Know the main lines: 4.e5 c5 5.a3 Bxc3+ 6.bxc3 leads to the famous unbalanced battles. Choose your style: 7.Qg4 poisoned pawn for chaos, 7.Nf3 for sanity. Study the endgames: many Winawers simplify to technical endings. Respect the bishop pair: Black\u2019s compensation is real \u2014 don\u2019t grab and hope.'],
['A complete anti-London system','chess-opening','Meet the London with ...c5, ...Qb6, and ...Bf5 pressure instead of passive acceptance.','Strike early: 1.d4 d5 2.Bf4 c5 challenges the setup at once. Develop actively: ...Nc6, ...Qb6, and ...Bf5 keep every piece busy. Know the traps: the London\u2019s Bxh7+ ideas fail against prepared kings. Counterattack: the London wants a slow game \u2014 give it a fast one.'],
['First-move advantage: playing the White pieces','chess-strategy','White scores about 55% at master level; the edge comes from the initiative, not material.','Seize the tempo: develop quickly and ask questions before Black is ready. Keep the initiative: every exchange should improve your position, not release tension. Know when to simplify: ahead in development, trade into better endings. Study model games: Morphy and Fischer show how initiative becomes attack.'],
['Converting a winning position','chess-strategy','Most games are lost by the winning side; technique is a trainable skill.','Simplify smartly: trade the opponent\u2019s most active pieces, not your attackers. Centralize the king: in endings the king is a fighting piece. Avoid counterplay: ask \u201cwhat is their only chance?\u201d and remove it. Practice: drill queen-vs-pawn and rook endings until they are automatic.'],
['Defending worse positions','chess-strategy','Bad positions are saved by activity, not passivity; create problems for the attacker.','Stay active: passive defense loses slowly and surely. Seek counterplay: even one threat changes the attacker\u2019s math. Trade attackers: exchanges ease the pressure. Use the clock: make them prove the win with little time.'],
['Playing the isolated queen pawn','chess-strategy','The IQP gives dynamic piece play at the cost of a long-term weakness; attack before the endgame.','Use the outposts: knights on e5 and c5 are the IQP\u2019s joy. Attack the king: the IQP side must play for mate or a crushing attack. Avoid simplification: every trade helps the blockader. Know the blockade: if they blockade with a knight, change plans.'],
['Hanging pawns: asset or liability','chess-strategy','The c4/d4 duo can steamroll or collapse; advance them with piece support or trade one off.','Support the push: rooks behind, pieces aiming at the break squares. Time the advance: push when your pieces are ready, not before. Accept the trade: sometimes c5 or d5 alone is the right structure. Study the classics: the hanging pawns decided countless Karpov games.'],
['The art of the exchange sacrifice','chess-strategy','Rook for minor piece can be winning when it kills the opponent\u2019s best defender or seizes key squares.','Identify the target: which enemy piece is truly essential? Calculate the follow-up: the sacrifice must create lasting pressure. Trust the compensation: initiative plus structure beats the exchange. Learn from Tal and Shirov: the masters of beautiful destruction.'],
['Prophylaxis in practice','chess-strategy','Ask what the opponent wants before deciding what you want; prevention is invisible mastery.','List their ideas: candidate moves for the opponent first. Find the preventing move: one move that kills two plans is gold. Stay flexible: prophylaxis is not passivity \u2014 keep your own threats. Study Petrosian and Carlsen: the great preventers.'],
['Attacking the castled king','chess-strategy','A successful kingside attack needs a pawn lever, piece concentration, and the defender\u2019s pieces far away.','Open a file: the h- or g-pawn lever cracks the shelter. Bring the pieces: queen, rooks, and a dark-squared bishop is the classic battery. Count the defenders: attack when they are outnumbered. Sacrifice to open: the Greek Gift (Bxh7+) is the eternal pattern.'],
['Endgame technique: rook endings','chess-strategy','Rook endings are the most common and most misplayed; activity beats material.','Activate the rook: behind passed pawns, on the seventh, cutting off the king. Use the king: centralize aggressively. Know the draws: Philidor and second-rank defense save lost positions. Study the Lucena: the winning bridge every player must know.'],
['Time management in tournament chess','chess-strategy','The clock is a piece; budget thinking time by position type, not by move number.','Spend in the critical moments: middlegame crossroads deserve the minutes. Move fast in theory: known positions should cost seconds. Keep a reserve: never drop below five minutes before move 30. Practice: play training games at the tournament time control.'],
['Blitz and bullet survival guide','chess-strategy','Speed chess rewards openings you know, premoves, and flagging technique.','Play your repertoire: no experiments at speed. Premoves wisely: only safe recaptures and forced moves. Manage the clock: ahead on time, keep pieces on; behind, complicate. Stay calm: mouse slips happen \u2014 the next game starts in seconds.'],
['How to analyze your own games','chess-strategy','Engine-free first, engine second: your mistakes teach more than the computer\u2019s.','Annotate alone: find the critical moments and your candidate moves. Ask why: every blunder has a thinking error behind it. Check with the engine: verify, don\u2019t outsource judgment. Log patterns: one recurring mistake fixed is worth ten wins.'],
['Playing against higher-rated opponents','chess-strategy','Stronger players punish passivity; play your game and make them prove their rating.','Play principled chess: solid openings, no cheap traps. Create complications: favorites hate chaos against underdogs. Use your preparation: surprise value is real. Learn regardless: every loss to a master is a lesson.'],
['The psychology of the swindle','chess-strategy','Lost positions are saved by problems, not hope; set traps the attacker must solve.','Stay tricky: checks, captures, and threats force accuracy. Offer the wrong win: tempt them into your preparation. Keep the clock in play: time pressure breeds blunders. Never resign early: grandmasters swindle grandmasters.'],
['Pawn storms: when and how','chess-strategy','Storm the enemy king with pawns when your king is safe and your pieces support the advance.','Secure your king: castle long or keep the center closed first. Push with support: every pawn advance needs a piece behind it. Open lines at the right moment: the break, not the push, wins. Study the Yugoslav: the Dragon\u2019s g4-g5 model.']
];
var GAME_MECHANICS = ['deck-building','worker placement','tile-laying','auction and bidding','area majority','set collection','push-your-luck','cooperative play','hidden roles','route building','engine building','drafting','trick-taking','roll-and-write','asymmetric powers','legacy campaign','deduction','hand management','grid movement','resource conversion'];
var GAME_THEMES = ['deep-sea exploration','a floating market','clockwork cities','migrating birds','an ancient library','desert caravans','lunar colonies','a night bakery','volcano islands','a traveling circus','mushroom forests','arctic research stations','a haunted hotel','river deltas','sky pirates','a seed vault','glacier expeditions','a lighthouse network','monsoon cities','an orchid conservatory'];
var GT_A = ['Ember','Gilded','Hollow','Copper','Velvet','Iron','Paper','Silent','Crimson','Golden','Obsidian','Amber','Driftwood','Starfall','Moonlit','Thunder','Willow','Foxglove','Brass','Lantern'];
var GT_B = ['Harbor','Expedition','Cartographers','Emporium','Voyage','Archives','Meridian','Confluence','Outpost','Regatta','Bazaar','Crossing','Atlas','Tide','Summit','Grove','Circuit','Horizon','Depot','Requiem'];
var RULE_TOPICS = [
['How to run a Swiss tournament','Running a fair Swiss event: pair by score, avoid rematches, and publish standings every round.','Seed the field: rank players by rating for round one. Pair by score: top half vs bottom half within each score group, colors balanced. Avoid repeats: no rematch pairings, ever. Publish and repeat: post standings, collect results, pair the next round.'],
['Bughouse rules','The two-board chaos variant: captured pieces are passed to your partner to drop.','Form teams: partners sit back-to-back at adjacent boards. Pass the captures: your takes become your partner\u2019s drops. Play fast: bughouse lives on blitz clocks. Coordinate: call for the piece you need \u2014 loudly.'],
['Chess boxing? No \u2014 chess puzzles for kids','Teach tactics through puzzles: mates in one, then forks, then pins.','Start with mates in one: the instant reward hooks young minds. Add one motif weekly: fork, pin, skewer in rotation. Celebrate streaks: puzzle rush scores motivate. Keep it short: fifteen focused minutes beats an hour of drift.'],
['Setting up a chess club','A thriving club needs a venue, sets, a ladder, and one weekly ritual.','Find the room: libraries and cafes welcome clubs. Stock the sets: ten boards covers most nights. Run a ladder: challenge-based rankings keep it spicy. Teach weekly: one fifteen-minute lesson per meeting grows everyone.'],
['Streaming your board game night','Share the table online: one overhead camera and one rules explainer.','Mount the camera: overhead on a boom shows the whole board. Mic the table: one room mic beats four bad ones. Teach on stream: explain rules as you play. Engage chat: let viewers vote on the tough calls.'],
['Teaching games to new players','The best teach: hook, play, then rules-deep-dive.','Hook first: one sentence on what you do and why it\u2019s fun. Start playing: teach the turn structure, then begin. Layer the rules: add exceptions when they arise. Let them win-ish: play openly, not ruthlessly, the first game.'],
['Sleeving and storing a collection','Protect the investment: sleeve the shuffled, box the rest.','Sleeve what shuffles: cards that see play get protection. Box by size: standard storage fits standard games. Label everything: future-you thanks present-you. Cull yearly: trade the unplayed.'],
['Designing your first board game','Start with the core loop: one interesting decision, repeated.','Find the decision: what does a player choose every turn? Prototype ugly: index cards beat art. Playtest early: strangers, not friends, give truth. Iterate ruthlessly: kill your darlings weekly.'],
['Running a learn-to-play event','Teach ten strangers a new game in an hour: structure is everything.','Pick the right game: thirty-minute teach maximum. Set the tables: one teacher per four players. Demo first: play two open rounds together. Debrief: ask what clicked and what confused.'],
['Caring for a wooden chess set','Wood rewards care: stable humidity, soft cloths, and no sunlight.','Control the climate: avoid attics and damp basements. Dust gently: soft brush, never water. Oil sparingly: a light wax once a year. Store boxed: pieces in felt, board flat.']
];
function sigOpening(r, id, seed) {
  var t = pick(REP_TOPICS.filter(function (x) { return x[1] === 'chess-opening'; }), r);
  var secs = [{ heading: 'The idea', body: t[0] + '. ' + t[2] }, { heading: 'In practice', body: t[3] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature repertoire guide', category: 'chess-opening', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { topic: t[1], key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown repertoire guide.', related: [], _seed: seed };
}
function sigStrategy(r, id, seed) {
  var t = pick(REP_TOPICS.filter(function (x) { return x[1] === 'chess-strategy'; }), r);
  var secs = [{ heading: 'The idea', body: t[0] + '. ' + t[2] }, { heading: 'In practice', body: t[3] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature lesson', category: 'chess-strategy', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { topic: 'chess-strategy', key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown strategy lesson.', related: [], _seed: seed };
}
function sigGame(r, id, seed) {
  var title = 'The ' + pick(GT_A, r) + ' ' + pick(GT_B, r);
  var players = pick(['2', '2\u20134', '3\u20135', '2\u20136', '1\u20134', '3\u20136'], r);
  var mechs = shuffle(GAME_MECHANICS, r).slice(0, ri(r, 2, 3));
  var theme = pick(GAME_THEMES, r);
  var mins = ri(r, 20, 120);
  var secs = [
    { heading: 'The game', body: title + ' is a Signature homegrown board game for ' + players + ' players (about ' + mins + ' minutes), set among ' + theme + '. Its heart is ' + mechs.join(' and ') + '.' },
    { heading: 'How it plays', body: 'Each round, players ' + pick(['draft cards to shape their strategy, then spend them to claim key spaces', 'place workers to gather resources, then convert them along personal engine tracks', 'bid for turn order, then expand across the shared map', 'draw tiles and build the board together, scoring patterns as they emerge'], r) + '. Tension builds as ' + pick(['the shared pool drains', 'the event deck escalates', 'rival engines come online', 'the map fills and options narrow'], r) + ', until ' + pick(['the final scoring rewards the boldest engine', 'one player triggers the endgame and everyone counts their legacy', 'the last round becomes a knife-fight for majority bonuses'], r) + '.' },
    { heading: 'Why it works', body: 'The design pairs a beloved theme (' + theme + ') with tight mechanisms (' + mechs.join(', ') + '), so every turn offers a genuine decision and every game tells a different story.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: title, category: 'board-game', record_kind: RECORD_KIND, origin: 'signature-generated', summary: 'A homegrown ' + players + '-player game of ' + mechs.join(' and ') + ', set among ' + theme + '.', details: { players: players, play_time_minutes: mins, mechanisms: mechs, theme: theme }, sections: secs, record_text: text, source_note: 'Signature-generated: an original homegrown game design.', related: [], _seed: seed };
}
function sigRules(r, id, seed) {
  var t = pick(RULE_TOPICS, r);
  var secs = [{ heading: 'Overview', body: t[0] + '. ' + t[1] }, { heading: 'Procedure', body: t[2] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature guide', category: 'game-rules', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[1], details: { area: 'game-rules', key_points: t[1].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown gaming guide.', related: [], _seed: seed };
}
var REAL = interleave([
  REAL_OPENINGS.map(function (e) { return { k: 'o', e: e }; }),
  REAL_STRATEGY.map(function (e) { return { k: 's', e: e }; }),
  REAL_GAMES.map(function (e) { return { k: 'g', e: e }; }),
  REAL_RULES.map(function (e) { return { k: 'r', e: e }; })
]);
function realOpening(e, id, seed) {
  var secs = [
    { heading: 'The opening', body: e[0] + ' (' + e[1] + '): ' + e[2] + '. ' + e[3] },
    { heading: 'How to play it', body: 'Learn the tabiyas \u2014 the standard positions arising near move 10\u201315 \u2014 then study the characteristic middlegame plans: which pawn breaks, which piece maneuvers, and which endgames favor each side. Play practice games from the tabiya before memorizing deeper lines.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'chess-opening', record_kind: RECORD_KIND, origin: 'sourced', summary: e[3], details: { eco: e[1], moves: e[2] }, sections: secs, record_text: text, source_note: 'Sourced: standard opening theory (ECO codes and main lines).', related: [], _seed: seed };
}
function realStrategy(e, id, seed) {
  var secs = [{ heading: 'The concept', body: e[0] + ' (' + e[1] + '). ' + e[2] }, { heading: 'Training it', body: 'Drill this theme in puzzles and slow games: set up positions featuring ' + e[0].toLowerCase() + ', play them against the computer from both sides, and review where the idea decided the game.' }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'chess-strategy', record_kind: RECORD_KIND, origin: 'sourced', summary: e[2], details: { topic: e[1] }, sections: secs, record_text: text, source_note: 'Sourced: standard chess instruction.', related: [], _seed: seed };
}
function realGame(e, id, seed) {
  var byline = (e[3] ? ' Designed by ' + e[3] : '') + (e[2] ? ' (' + e[2] + ')' : '');
  var secs = [
    { heading: 'The game', body: e[0] + ' \u2014 for ' + e[1] + ' players.' + byline + ' ' + e[4] },
    { heading: 'At the table', body: 'Expect ' + e[4].split('.')[0].toLowerCase() + '. New players should learn the core loop first: what you do on a turn, how you score, and how the game ends \u2014 the rest can be layered in as play proceeds.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'board-game', record_kind: RECORD_KIND, origin: 'sourced', summary: e[4], details: { players: e[1], year: e[2], designer: e[3] }, sections: secs, record_text: text, source_note: 'Sourced: published game facts; verify edition details against publisher listings.', related: [], _seed: seed };
}
function realRules(e, id, seed) {
  var secs = [{ heading: 'The rules', body: e[0] + '. ' + e[1] }, { heading: 'In practice', body: 'Apply these rules consistently in casual and club play; in tournaments, the arbiter\u2019s ruling and the official laws of the organizing body are final.' }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'game-rules', record_kind: RECORD_KIND, origin: 'sourced', summary: e[1], details: { area: 'game-rules' }, sections: secs, record_text: text, source_note: 'Sourced: standard laws and rules of play.', related: [], _seed: seed };
}
var CATMAP = { o: 'chess-opening', s: 'chess-strategy', g: 'board-game', r: 'game-rules' };
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (!opts.category || CATMAP[re.k] === opts.category) {
      if (re.k === 'o') return realOpening(re.e, id, seed);
      if (re.k === 's') return realStrategy(re.e, id, seed);
      if (re.k === 'g') return realGame(re.e, id, seed);
      return realRules(re.e, id, seed);
    }
  }
  var cat = opts.category || pick(CATS, rnd);
  if (cat === 'chess-opening') return sigOpening(rnd, id, seed);
  if (cat === 'chess-strategy') return sigStrategy(rnd, id, seed);
  if (cat === 'board-game') return sigGame(rnd, id, seed);
  return sigRules(rnd, id, seed);
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-CHS-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  return { ok: errors.length === 0, errors: errors };
}
function driftCheck(rec, sample) {
  var errors = [];
  for (var i = 0; i < sample.length; i++) {
    if (sample[i] && sample[i].t === rec.title && sample[i].id !== rec.id) { errors.push('duplicate title in archive sample'); break; }
  }
  return { ok: errors.length === 0, errors: errors };
}
var GEN = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, slug: SLUG, prefix: PREFIX, categories: CATS, record_kind: RECORD_KIND, realCount: REAL.length };
if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, GEN);
if (typeof module !== 'undefined' && module.exports) module.exports = GEN;
})();
