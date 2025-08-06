const canvas = document.getElementsByClassName("enikki__drawing-canvas")[0]
const sdb = SimpleDrawingBoard.create(canvas)

sdb.setLineSize(4);
sdb.setLineColor("blue");

const targets = ["red", "orange", "yellow", "green", "blue", "black"]

for (let i = 0; i < targets.length; i++) {
  const target = targets[i]
  const element = document.getElementById(target)
  element.addEventListener("click", () => {
    if (sdb.mode == "erase") {
      sdb.toggleMode()
    }
    sdb.setLineColor(target)
  })
}

const colorPicker = document.getElementById("color-picker");
colorPicker.addEventListener("input", (e) => {
  if (sdb.mode == "erase") {
    sdb.toggleMode()
  }
  sdb.setLineColor(e.target.value);
});

const eraser = document.getElementById("eraser-container")

eraser.addEventListener("click", () => {
  if (sdb.mode == "draw") {
    sdb.toggleMode()
  }
})

document.getElementById("submit-button").addEventListener("click", async () => {
  const content = document.getElementsByClassName("enikki__content")[0].value
  if (content == null || content.length == 0) {
    alert("空では提出できません")
    return
  }
  canvas.toBlob((blob) => {
    const formData = new FormData();
    formData.set("content", content)
    formData.append("image", blob, "canvas.png");
    fetch("/create", {
      method: "POST",
      body: formData,
      redirect: 'follow'
    })
      .then(res => {
        if (res.redirected) {
          window.location.href = res.url;
        }
      });
  },
    "image/png")
})
