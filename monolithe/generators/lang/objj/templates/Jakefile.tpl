{{ header }}

var ENV = require("system").env,
    FILE = require("file"),
    OS = require("os"),
    JAKE = require("jake"),
    task = JAKE.task,
    CLEAN = require("jake/clean").CLEAN,
    FileList = JAKE.FileList,
    framework = require("cappuccino/jake").framework,
    configuration = ENV["CONFIG"] || ENV["CONFIGURATION"] || ENV["c"] || "Release";

framework ("{{ name }}", function(task)
{
    task.setBuildIntermediatesPath(FILE.join(ENV["CAPP_BUILD"], "{{ name }}.build", configuration));
    task.setBuildPath(FILE.join(ENV["CAPP_BUILD"], configuration));

    task.setProductName("{{ name }}");
    task.setIdentifier("io.monolithe.{{name}}");
    task.setVersion("1.0");
    task.setAuthor("{{ author }}");
    task.setEmail("{{ email }}");
    task.setSummary("{{ name }}");
    task.setSources(new FileList("*.j", "Fetchers/*.j"));
    task.setResources(new FileList("Resources/**/**"));
    task.setInfoPlistPath("Info.plist");

    if (configuration === "Debug")
        task.setCompilerFlags("-DDEBUG -g");
    else
        task.setCompilerFlags("-O2");
});

task("build", ["{{ name }}"]);

task("debug", function()
{
    ENV["CONFIG"] = "Debug"
    JAKE.subjake(["."], "build", ENV);
});

task("release", function()
{
    ENV["CONFIG"] = "Release"
    JAKE.subjake(["."], "build", ENV);
});

task ("documentation", function()
{
   OS.system("doxygen {{ name }}.doxygen")
});

task("test", ["test-only"]);

task("test-only", function()
{
    ENV["OBJJ_INCLUDE_PATHS"] = "Frameworks";

    OS.system("capp gen -fl . --force");

    var tests = new FileList('Test/*Test.j'),
        cmd = ["ojtest"].concat(tests.items()),
        cmdString = cmd.map(OS.enquote).join(" "),
        code = OS.system(cmdString);

    OS.system("rm -rf Frameworks");

    if (code !== 0)
        OS.exit(code);
});

task ("default", ["release"]);
task ("docs", ["documentation"]);
task ("all", ["release", "debug", "documentation"]);
