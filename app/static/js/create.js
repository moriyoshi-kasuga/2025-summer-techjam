const sdb = SimpleDrawingBoard.create(document.getElementsByClassName("enikki__drawing-canvas")[0])

sdb.setLineSize(4);
sdb.setLineColor("blue");

const targets = ["red", "orange", "yellow", "green", "blue", "black"]

for (let i = 0; i < targets.length; i++) {
  const target = targets[i]
  const element = document.getElementById(target)
  if (element == null) {
    console.log("not found: ", target)
  }
  element.addEventListener("click", () => {
    if (sdb.mode == "erase") {
      sdb.toggleMode()
    }
    sdb.setLineColor(target)
  })
}

const eraser = document.getElementById("eraser-container")

eraser.addEventListener("click", () => {
  if (sdb.mode == "draw") {
    sdb.toggleMode()
  }
})
