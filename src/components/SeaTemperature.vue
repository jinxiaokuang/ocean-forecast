<template>
  <canvas id="SeaTemperature" width="70" height="300" style="border:1px solid #000000;"></canvas>
</template>

<script>
export default {
  name: "SeaTemperature",
  mounted() {
    this.drawSeaTemperature();
  },
  methods: {
    drawSeaTemperature() {
      const c = document.getElementById("SeaTemperature");
      const ctx = c.getContext("2d");

      // 定义渐变颜色的存储对象数组 stops
      const stops = [
        { position: 0.01, color: 'rgb(255,23,13)' },
        { position: 0.3, color: 'rgb(255,255,0)' },
        { position: 0.4, color: 'rgb(0,255,0)' },
        { position: 0.65, color: 'rgb(0,255,255)' },
        { position: 0.85, color: 'rgb(65,105,225)' },
        { position: 1, color: 'rgb(138,43,226)' }
      ];

      // 创建渐变色对象，并把存储在 stops 中的颜色加入渐变色对象
      const gradient = ctx.createLinearGradient(10, 30, 30, 300);
      for (let i = 0; i < stops.length; i++) {
        gradient.addColorStop(stops[i].position, stops[i].color);
      }
      ctx.fillStyle = gradient;

      // 将渐变色对象填充到画布上
      ctx.fillRect(10, 50, 20, 240);

      // 绘制标记线和文本
      ctx.font = "13px Arial";
      ctx.fillStyle = "black"; // 设置文本颜色
      ctx.fillText("海温:°C", 10, 30);
      ctx.fillText("32", 50, 55);
      ctx.fillText("28", 50, 80);
      ctx.fillText("24", 50, 105);
      ctx.fillText("18", 50, 160);
      ctx.fillText("8", 55, 235);
      ctx.fillText("4", 55, 260);
      ctx.fillText("0", 55, 282);
      ctx.fillText("-2", 50, 295);

      ctx.strokeStyle = "black"; // 设置线条颜色
      ctx.moveTo(40, 50);
      ctx.lineTo(45, 50);
      ctx.moveTo(40, 75);
      ctx.lineTo(45, 75);
      ctx.moveTo(40, 100);
      ctx.lineTo(45, 100);
      ctx.moveTo(40, 155);
      ctx.lineTo(45, 155);
      ctx.moveTo(40, 230);
      ctx.lineTo(45, 230);
      ctx.moveTo(40, 255);
      ctx.lineTo(45, 255);
      ctx.moveTo(40, 280);
      ctx.lineTo(45, 280);
      ctx.moveTo(40, 290);
      ctx.lineTo(45, 290);
      ctx.moveTo(40, 50);
      ctx.lineTo(40, 290);
      ctx.stroke();
    }
  }
}
</script>
<style>
  #SeaTemperature {
    position: absolute;
    top: 500px;
    left: 150px;
    z-index: 5; /* 确保在地图上面显示 */
    background: rgba(255, 255, 255); /* 背景色使其在地图上更加可见 */
  }
</style>