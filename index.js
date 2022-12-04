const fs = require("fs");
const path = require("path");
const AdmZip = require("adm-zip");
const pyshell = require("python-shell");
const PythonShell = pyshell.PythonShell;
const gm = require("gm").subClass({ imageMagick: "7+" });

let comic = fs.readdirSync("./files/raw")[0];
console.log(comic);
let zip = new AdmZip("./files/raw/" + comic);

zip.extractAllTo("./files/temp/" + comic, true);
let images = fs.readdirSync("./files/temp/" + comic);
/*
// console.log(images);
// let cmd = ["convert"].concat(images);
// console.log(cmd);
// cmd = cmd.concat(["-append", "output.jpg"]);
// let gh = cmd.join(" ");
// console.log(gh);
/*const { spawn } = require("child_process");
const ls = spawn("gm", cmd, { cwd: "files/temp/" + comic });

ls.stdout.on("data", (data) => {
  console.log(`stdout: ${data}`);
});
console.log("/files/temp/" + comic + "/" + images[0]);

var gmstate = gm("./files/temp/" + comic + "/" + images[0]);
for (var i = 1; i < images.length; i++)
  gmstate.append("./files/temp/" + comic + "/" + images[i]);

// finally write out the file asynchronously
gmstate.write("result.jpg", function (err) {
  if (!err) console.log("Hooray!");
  else console.log(err);
});
*/
let lang = "korean";
console.log(images);
let options = {
  // get print results in real-time
  mode: "text",
  pythonOptions: ["-u"],
  args: [comic, lang, images],
};

PythonShell.run("join.py", options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log(results);
});
