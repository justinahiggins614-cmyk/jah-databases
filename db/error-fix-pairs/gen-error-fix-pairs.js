/* JAH Error Fix Database generator. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['python','javascript','sql','git','docker','api'];
var FILES=['app.py','main.py','server.py','utils.py','handler.py','worker.py','config.py'];
var JSFILES=['app.js','index.js','server.js','utils.js','api.js','client.js'];
var VARS=['user','data','result','items','config','resp','count','name','rows','opts'];
function T(s,r){return s.replace(/\{N\}/g,ri(r,1,999)).replace(/\{F\}/g,pick(r,FILES)).replace(/\{J\}/g,pick(r,JSFILES)).replace(/\{V\}/g,pick(r,VARS)).replace(/\{P\}/g,ri(r,1024,9999)).replace(/\{L\}/g,ri(r,2,400));}
var E={
python:[
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    {V} = unknown_func()\nNameError: name \'unknown_func\' is not defined','A script crashes the moment it reaches a function call in {F}.','The name was never defined or the defining import was removed, so Python cannot resolve it at call time.','Define the function before use, or add the missing import (e.g. `from helpers import unknown_func`) at the top of {F}, then rerun.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    total = count + "5"\nTypeError: unsupported operand type(s) for +: \'int\' and \'str\'','Adding a number to user input in {F} raises a TypeError.','The input arrived as a string and was added to an int without conversion.','Wrap the input with int() or float() first (e.g. `total = count + int(raw)`), or validate the input before arithmetic.','medium'],
['  File "{F}", line {N}\n    if x == 1\n              ^\nSyntaxError: expected \':\'','The file {F} will not even start parsing.','A colon is missing after the `if` condition, which Python requires.','Add the colon: `if x == 1:` and re-indent the block underneath.','low'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    print({V}["key"])\nKeyError: \'key\'','Looking up a dict key in {F} fails at runtime.','The dictionary {V} does not contain \'key\' — the key was never inserted or was removed upstream.','Use {V}.get("key", default) for a safe lookup, or guard with `if "key" in {V}:` before access.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    first = {V}[0]\nIndexError: list index out of range','Reading the first element of a list in {F} crashes.','The list {V} is empty at that point, so index 0 does not exist.','Guard with `if {V}:` before indexing, or use a default: `first = {V}[0] if {V} else None`.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    import missinglib\nModuleNotFoundError: No module named \'missinglib\'','{F} fails on its first import line.','The third-party package is not installed in the active Python environment.','Install it into the right environment: `pip install missinglib`, and confirm with `pip show missinglib`.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    {V}.append(x)\nAttributeError: \'NoneType\' object has no attribute \'append\'','A method call on {V} in {F} raises AttributeError.','{V} is None — the earlier call that should have produced a list returned None instead.','Trace where {V} is assigned; return the list instead of None, or initialize `{V} = []` before the loop.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    avg = total / 0\nZeroDivisionError: division by zero','A division in {F} crashes when the divisor is zero.','The divisor became 0 (empty dataset or a counter never incremented).','Guard the division: `avg = total / n if n else 0`, and investigate why the divisor is zero.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    open("missing.txt")\nFileNotFoundError: [Errno 2] No such file or directory: \'missing.txt\'','{F} tries to open a file that is not there.','The path is wrong relative to the working directory, or the file was never created.','Use an absolute path or resolve it with pathlib relative to __file__; create the file first if it should exist.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in parse\n    json.loads(raw)\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)','Parsing JSON in {F} fails on an empty response.','The response body was empty (or HTML), so there is no JSON to parse.','Check the HTTP status and content-type before parsing; log the raw body to see what the server actually sent.','medium'],
['    def handler():\n        x = 1\n      y = 2\nIndentationError: unindent does not match any outer indentation level','{F} has an inconsistent indent at line {N}.','Tabs and spaces were mixed (or a block was dedented by a stray amount).','Re-indent using spaces only (4 per level); most editors can convert tabs to spaces automatically.','low'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    result = recurse()\nRecursionError: maximum recursion depth exceeded','{F} dies in a recursive call at line {N}.','The recursion has no working base case, so it calls itself forever.','Add a terminating base case, or rewrite iteratively; as a stopgap, `sys.setrecursionlimit` only delays the crash.','high'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    text.decode("utf-8")\nUnicodeDecodeError: \'utf-8\' codec can\'t decode byte 0xff in position 0','Decoding bytes in {F} raises a codec error.','The bytes are not UTF-8 (e.g. a Latin-1 or UTF-16 file) or are binary data.','Open with the correct encoding (`open(..., encoding="latin-1")`) or `errors="replace"`; inspect the file\'s real encoding first.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in run\n    assert status == "ok"\nAssertionError','An assertion in {F} fires during a run.','The invariant being asserted is genuinely violated (or the assertion itself is wrong).','Read the values at the assertion; fix the logic upstream, or correct the assertion if the expectation was outdated.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in worker\n    print(counter)\nUnboundLocalError: local variable \'counter\' referenced before assignment','{F} reads `counter` before it is assigned in the function.','Assigning to `counter` later in the function makes Python treat it as local everywhere in that scope.','Add `global counter` (or `nonlocal`) at the top of the function, or pass the value as a parameter.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    from pkg import thing\nImportError: cannot import name \'thing\' from \'pkg\'','An import from `pkg` in {F} fails.','The name does not exist in that package version (renamed or moved).','Check the installed package version and its docs; import the renamed symbol or pin the expected version.','medium'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    row = next(it)\nStopIteration','Calling next() on an exhausted iterator in {F} raises StopIteration.','The iterator is empty — all items were already consumed.','Use `next(it, default)` with a fallback, or check for remaining items before calling next().','low'],
['Traceback (most recent call last):\n  File "{F}", line {N}, in <module>\n    os.remove("locked.txt")\nPermissionError: [Errno 13] Permission denied: \'locked.txt\'','Deleting a file in {F} is denied.','The process lacks permission, or the file is open/locked by another program.','Close other handles to the file, run with the right user, or fix ownership with chown/chmod.','medium'],
['  File "{F}", line {N}\n    return\n         ^\nSyntaxError: \'return\' outside function','A bare `return` sits at module level in {F}.','The return statement was dedented out of its function or pasted at top level.','Move the `return` back inside the function body it belongs to.','low']
],
javascript:[
['TypeError: Cannot read properties of undefined (reading \'{V}\')\n    at render ({J}:{N}:{L})','The page crashes in render() inside {J}.','An object expected to exist (API response, prop, or DOM node) is undefined when the code reads .{V}.','Add a guard (`obj && obj.{V}` or optional chaining `obj?.{V}`) and trace why the object is undefined.','high'],
['SyntaxError: Unexpected token \'}\' in JSON at position {N}\n    at JSON.parse (<anonymous>)','JSON.parse throws while handling a server response.','The response is not valid JSON (often an HTML error page from the server).','Log the raw response text first; only parse when the content-type is JSON and the status is OK.','medium'],
['ReferenceError: {V} is not defined\n    at init ({J}:{N}:{L})','{J} throws the moment init() runs.','{V} was never declared (typo, missing import, or a script tag that failed to load).','Declare/import {V} before use; check the network tab to confirm the defining script actually loaded.','high'],
['RangeError: Maximum call stack size exceeded\n    at walk ({J}:{N}:{L})','The browser tab freezes, then {J} throws a stack error.','walk() recurses without a base case (often on circular data).','Add a base case / visited-set; for deep data, rewrite iteratively.','high'],
['Uncaught (in promise) TypeError: fetch failed\n    at loadData ({J}:{N}:{L})','A fetch() call in {J} rejects with a network error.','The request never completed: server down, wrong URL, or CORS/offline.','Catch the rejection with try/catch, check the URL and server status, and show a retry UI instead of crashing.','medium'],
['Access to fetch at \'https://api.example.com/data\' from origin \'https://app.example.com\' has been blocked by CORS policy','The browser blocks an API call from {J}.','The server does not send the required Access-Control-Allow-Origin header for this origin.','Enable CORS on the server for the app origin, or proxy the request through your own backend.','high'],
['TypeError: {V}.map is not a function\n    at list ({J}:{N}:{L})','Rendering a list in {J} throws on .map().','{V} is not an array here — it is an object, null, or a single item.','Normalize before mapping: `Array.isArray({V}) ? {V} : [{V}]`, and fix the producer to always send an array.','medium'],
['SyntaxError: Unexpected identifier\n    at {J}:{N}','{J} fails to parse entirely.','A keyword is misspelled, a comma is missing, or a reserved word is used as a variable name.','Read the exact line the parser points at; fix the token it chokes on.','low'],
['TypeError: Cannot assign to read only property \'{V}\' of object','Assigning to {V} in {J} throws in strict mode.','The property is frozen (Object.freeze) or defined read-only.','Create a copy with the change instead of mutating: `const next = {{...obj, {V}: val}}`.','medium'],
['Error: listen EADDRINUSE: address already in use :::3000\n    at Server.setupListenersOneByOne','The Node server in {J} will not start.','Port 3000 is already taken by another process.','Kill the process on that port (`lsof -ti:3000 | xargs kill`) or start on a free port.','medium'],
['TypeError [ERR_INVALID_ARG_TYPE]: The "path" argument must be of type string. Received undefined','A Node fs call in {J} throws a type error.','The path argument is undefined (missing config/env variable).','Default the value (`const p = process.env.P || "./data"`) and fail fast with a clear message when it is missing.','medium'],
['ReferenceError: window is not defined\n    at render ({J}:{N}:{L})','Server-side rendering in {J} crashes.','Browser-only globals like window/localStorage do not exist on the server.','Guard usage: `if (typeof window !== "undefined")`, or move the code into a client-only effect.','medium'],
['SyntaxError: await is only valid in async functions and the top level bodies of modules','An await in {J} fails to parse.','The enclosing function is not declared async.','Add `async` to the function declaration, or use promise chaining instead of await.','low'],
['TypeError: Converting circular structure to JSON','JSON.stringify in {J} throws on circular data.','The object references itself (parent/child links), which JSON cannot represent.','Strip the circular links first, or pass a replacer/seen-set to JSON.stringify.','medium'],
['Error: Cannot find module \'./{V}\'\n    at require ({J}:{N}:{L})','Node cannot resolve a require in {J}.','The path is wrong or the file extension was omitted/mistyped.','Fix the relative path (count the `../` levels) and include the exact filename.','medium']
],
sql:[
['ERROR: syntax error at or near "FROM"\nLINE {N}: SELECT name, FROM users;','A query fails to parse at line {N}.','There is a trailing comma after `name` before FROM.','Remove the trailing comma: `SELECT name FROM users;`.','low'],
['ERROR: relation "users" does not exist\nLINE {N}: SELECT * FROM users;','Querying `users` raises "relation does not exist".','The table is in another schema, is misspelled, or was never created in this database.','Schema-qualify it (`SELECT * FROM public.users`) or create/migrate the table first.','medium'],
['ERROR: column reference "id" is ambiguous\nLINE {N}: SELECT id FROM users JOIN orders ON users.id = orders.user_id;','A join query cannot tell which `id` is meant.','Both joined tables have an `id` column and the select list does not qualify it.','Qualify every column: `SELECT users.id ...` (or alias the tables and use the aliases).','low'],
['ERROR: insert or update on table "orders" violates foreign key constraint "orders_user_id_fkey"','An INSERT into orders is rejected.','The referenced user_id does not exist in the users table.','Insert the parent user row first, or correct the user_id being inserted.','medium'],
['ERROR: duplicate key value violates unique constraint "users_email_key"','Inserting a user fails on the email unique constraint.','That email already exists in the table.','Upsert instead (`INSERT ... ON CONFLICT (email) DO UPDATE`), or check existence first.','medium'],
['ERROR: deadlock detected\nDETAIL: Process {N} waits for ShareLock on transaction {P}; blocked by process {L}.','Two transactions deadlock and one is aborted.','The transactions lock the same rows in opposite order.','Retry the aborted transaction; order all writes the same way everywhere to stop it recurring.','high'],
['ERROR: division by zero','A computed column divides by zero.','A denominator (often COUNT of an empty group) is 0.','Use `NULLIF(denom, 0)` or `CASE WHEN denom = 0 THEN NULL ELSE num/denom END`.','medium'],
['ERROR: could not connect to server: Connection refused\nIs the server running on host "localhost" and accepting TCP/IP connections on port 5432?','The client cannot reach the database at all.','Postgres is not running, or it is not listening on that host/port.','Start the server, confirm the port in postgresql.conf, and check pg_hba.conf allows the connection.','critical'],
['ERROR: column "total" does not exist\nLINE {N}: SELECT total FROM (SELECT sum(amount) AS s FROM sales) t;','The outer query references a column the subquery never produced.','The subquery aliases the column as `s`, not `total`.','Reference the real alias (`SELECT s FROM ...`) or rename the alias to total.','low'],
['ERROR: current transaction is aborted, commands ignored until end of transaction block','Every statement after one failure is rejected.','An earlier statement errored, poisoning the whole transaction.','ROLLBACK and rerun; in code, wrap the transaction and roll back on any error.','medium'],
['ERROR: value too long for type character varying({N})','An INSERT is rejected for an overlong string.','The value exceeds the column\'s varchar limit.','Widen the column (`ALTER TABLE ... TYPE varchar({P})`) or validate/truncate input before insert.','medium'],
['ERROR: invalid input syntax for type integer: "{V}"','Casting \'{V}\' to integer fails.','Non-numeric text reached a numeric column (bad import or missing cast).','Clean the data first (`NULLIF`, regex filter) and cast explicitly: `{V}::integer` after validation.','medium']
],
git:[
['error: failed to push some refs to \'origin\'\nhint: Updates were rejected because the remote contains work that you do not have locally.','A git push is rejected as non-fast-forward.','Someone pushed to the branch after your last pull.','Run `git pull --rebase`, resolve any conflicts, then push again.','medium'],
['CONFLICT (content): Merge conflict in {F}\nAutomatic merge failed; fix conflicts and then commit the result.','A merge stops with conflicts in {F}.','Both sides edited the same lines of {F}.','Open {F}, pick the correct hunks between <<<<<<< and >>>>>>>, `git add {F}`, then `git commit`.','medium'],
['fatal: not a git repository (or any of the parent directories): .git','Every git command fails in this directory.','You are not inside a git working tree (wrong directory).','`cd` into the repository first, or run `git init` if this should be a new repo.','low'],
['error: Your local changes to the following files would be overwritten by merge:\n\t{F}\nPlease commit your changes or stash them before you merge.','A pull refuses to overwrite local edits to {F}.','Uncommitted local changes conflict with incoming changes.','`git stash`, pull, then `git stash pop`; or commit the local work first.','medium'],
['fatal: refusing to merge unrelated histories','Merging two repos fails outright.','The branches share no common ancestor commit.','If the merge is intentional: `git merge --allow-unrelated-histories`; otherwise clone the right repo.','medium'],
['error: src refspec main does not match any','Pushing `main` fails with "src refspec".','The local branch is named differently (e.g. master) or has no commits yet.','Check `git branch`; push the real name (`git push origin master`) or make a first commit.','low'],
['Permission denied (publickey).\nfatal: Could not read from remote repository.','Push/pull over SSH fails with a key error.','No SSH key is offered, or the key is not added to the account.','Generate a key (`ssh-keygen`), add the public key to the hosting account, and test with `ssh -T git@host`.','high'],
['error: failed to push some refs — hint: its remote counterpart has diverged','Push is rejected after a rebase.','The rebase rewrote local history so the branches diverged.','Push with lease: `git push --force-with-lease` (only if no one else uses this branch).','high'],
['fatal: Unable to create \'.git/index.lock\': File exists.','Git commands fail with an index.lock error.','A previous git process crashed and left its lock file behind.','Verify no git process is running, then `rm -f .git/index.lock` and retry.','medium'],
['error: remote origin already exists.','Adding a remote named origin fails.','The name `origin` is already taken in this repo.','Use `git remote set-url origin <url>` to change the URL, or add under a new name.','low']
],
docker:[
['Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?','Every docker command fails to reach the daemon.','The Docker daemon is not running (or the user cannot reach its socket).','Start Docker Desktop / `sudo systemctl start docker`; on Linux, add your user to the `docker` group.','critical'],
['Error response from daemon: driver failed programming external connectivity: Bind for 0.0.0.0:{P} failed: port is already allocated','A container will not start on port {P}.','Another container or process already owns that host port.','Map a different host port (`-p {L}:{P}`) or stop the process holding port {P}.','medium'],
['Error response from daemon: pull access denied for myimage, repository does not exist','docker pull fails for `myimage`.','The image name or tag is wrong, or the registry needs login.','Fix the name/tag (`docker pull myimage:{N}`) or `docker login` for a private registry.','medium'],
['standard_init_linux.go: exec user process caused "exec format error"','The container exits immediately with an exec format error.','The image was built for a different CPU architecture (e.g. arm64 image on amd64).','Rebuild for the target platform (`docker build --platform linux/amd64`) or use a multi-arch image.','high'],
['ERROR: No space left on device','Builds and pulls fail with no space.','The Docker disk (images, containers, build cache) is full.','Prune: `docker system prune -a --volumes` (careful: deletes unused data), then rebuild.','high'],
['Error response from daemon: network mynet not found','docker run --network mynet fails.','The network `mynet` does not exist (typo or never created).','Create it (`docker network create mynet`) or fix the network name in the command/compose file.','medium'],
['Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock','Docker commands fail with permission denied.','Your user is not in the `docker` group.','`sudo usermod -aG docker $USER`, then log out and back in (never chmod 777 the socket).','medium'],
['COPY failed: file not found in build context','docker build fails on a COPY step.','The file is in .dockerignore or outside the build context directory.','Remove it from .dockerignore or move it under the context dir; check the exact COPY source path.','medium'],
['ERROR: The Compose file is invalid because: services.web.ports contains an invalid type','docker compose up rejects the compose file.','A ports entry is malformed (e.g. missing quotes around "{P}:{P}").','Quote port mappings in YAML: `ports: - "{P}:{P}"`, then validate with `docker compose config`.','low'],
['container exited with code 137','A container keeps dying with exit code 137.','It was OOM-killed: the container exceeded its memory limit.','Raise the limit (`--memory 2g` / compose `mem_limit`), or fix the memory leak in the app.','high']
],
api:[
['401 Unauthorized — {"error":"invalid_token","message":"The access token expired"}','API calls in {J} start returning 401.','The bearer token expired (or was revoked).','Refresh the token via the refresh endpoint and retry; store expiry and refresh proactively.','high'],
['429 Too Many Requests — {"error":"rate_limited","retry_after":{N}}','The API throttles calls from {J}.','The client exceeded the endpoint\'s rate limit.','Back off for retry_after seconds with jitter, then retry; batch or cache requests to stay under the limit.','medium'],
['404 Not Found — {"error":"no_such_resource"}','A GET to /v1/items/{N} returns 404.','The ID does not exist, or the path version/prefix is wrong.','Verify the ID exists (list endpoint) and the base URL/version; handle 404 as "not found", not a crash.','medium'],
['500 Internal Server Error — {"error":"unexpected"}','The API returns 500 for a request from {J}.','A server-side bug or a downstream outage on the provider\'s side.','Retry with exponential backoff; if it persists, reduce the request to a minimal repro and file a support ticket.','high'],
['Access to XMLHttpRequest blocked: preflight response has status 403','Browser calls from {J} fail the CORS preflight.','The server rejects OPTIONS requests or the required headers.','Fix the server to answer OPTIONS with 2xx and the right Allow-Headers; test with curl -X OPTIONS.','high'],
['SSL certificate problem: certificate has expired','HTTPS calls from {J} fail TLS verification.','The server\'s TLS certificate expired.','Renew the certificate on the server (e.g. certbot renew); do NOT disable verification in production.','critical'],
['FetchError: network timeout at: https://api.example.com/v1/slow (timeout {N}ms)','A slow endpoint times out in {J}.','The request exceeded the client timeout.','Raise the timeout for this call, add retries with backoff, and ask the provider about a faster/paginated endpoint.','medium'],
['400 Bad Request — {"error":"invalid_json","message":"Unexpected token at position {N}"}}','POSTing to the API returns 400 invalid_json.','The request body is malformed JSON (or the content-type header is missing).','JSON.stringify the body and set `Content-Type: application/json`; validate the payload before sending.','medium'],
['403 Forbidden — {"error":"insufficient_scope"}','An API call returns 403 despite a valid token.','The token lacks the required scope/permission for this endpoint.','Request the missing scope during auth, or use a token that already has it; check the API\'s scope docs.','medium'],
['502 Bad Gateway — upstream connect error','The API gateway returns 502 in {J}.','A proxy/gateway cannot reach the backend service.','Retry briefly (gateways flap); if steady, the backend is down — check the provider status page.','high']
]
};
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=opts.category||pick(rnd,CATS);
  var bank=E[cat]||E.python;
  var e=pick(rnd,bank);
  var et=T(e[0],rnd);
  var title=et.split('\n')[0].slice(0,80);
  return {
    id:'JAH-ERR-'+String(seed).padStart(6,'0'),
    error_id:'JAH-ERR-'+String(seed).padStart(6,'0'),
    error_text:et,
    context:T(e[1],rnd),
    root_cause:T(e[2],rnd),
    fix:T(e[3],rnd),
    language_or_tool:cat,
    severity:e[4],
    title:title
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','error_id','error_text','context','root_cause','fix','language_or_tool','severity','title'].forEach(function(k){if(!r[k])e.push('missing '+k);});
  if(r.id&&!/^JAH-ERR-\d{6}$/.test(r.id))e.push('bad id');
  if(r.error_id&&r.error_id!==r.id)e.push('error_id != id');
  if(r.language_or_tool&&CATS.indexOf(r.language_or_tool)<0)e.push('bad category');
  if(r.severity&&['low','medium','high','critical'].indexOf(r.severity)<0)e.push('bad severity');
  if(r.error_text&&(r.error_text.length<10||r.error_text.length>600))e.push('error_text length');
  if(r.title&&r.title.length>80)e.push('title too long');
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-error-fix-pairs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('error-fix-pairs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
