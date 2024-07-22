<template>
  <div class="container">
    <div id="mapTile" style="background-color: rgba(164, 205, 255, 1); position: relative;"></div>
  </div>
</template>

<script>
import L from "leaflet";
import 'leaflet/dist/leaflet.css';
import * as d3 from 'd3';
// // import chroma from 'chroma-js';
// import stops from "leaflet";

const wind = {
      name:'wind',
      numberArray:[3.5, 6.5, 9.5, 12.5, 15.5, 18.5],
      opacity: 1.0,
      width: 1.0,
      velocityScale: 0.0015,
      magnitude: true,
      direction: true,
      controlBar: false,
      colorBar: false,
};

export default {
  name: 'Map',
  data() {
    return {
      map: null
    }
  },
  methods: {
    initMap() {  // 地图初始化
      this.map = L.map("mapTile", {
        center: [33, 125],
        zoom: 5,
        minZoom: 4,
        maxZoom: 7,
        zoomControl: false,  // 禁用 + - 按钮
        doubleClickZoom: false,  // 禁用双击放大
        attributionControl: false  // 移除右下角 leaflet 标识
      });

      // 地图的矢量图层
      const tile = L.tileLayer('/mapTile/{z}/{x}/{y}.png', {
        zIndex: 100,
      }).addTo(this.map);

      // 地图的标记图层
      const label = L.tileLayer(
          "https://t4.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=a8479c5bd1fd7b84c5a72669ed79a95b", {
            zIndex: 200,
          }
      ).addTo(this.map);

      // 将矢量瓦片地图层与标签层置于顶部
      this.map.getPanes().overlayPane.appendChild(tile.getContainer());
      this.map.getPanes().overlayPane.appendChild(label.getContainer());
    },

    ShowAscFile() {
      d3.text('/Subset_Data/data/20210601/UT/orderUT_000.asc').then((u) => {
        d3.text('/Subset_Data/data/20210601/VT/orderVT_000.asc').then((v) => {
          const color = chroma.scale(stops.map(stop => stop.color)).domain(wind.numberArray);
          const vf = L.VectorField.fromASCIIGrids(u, v);

          L.canvasLayer.scalarField(vf.getScalarField("magnitude"), {
            color: color,
            opacity: 0.5,
            interpolate: true,
            inFilter: function (v) {
              return v !== -32767
            },
            zIndex: 500,
          }).addTo(this.map);

          L.canvasLayer.vectorFieldAnim(vf, {
            width: wind.width,
            velocityScale: wind.velocityScale,
            inFilter: function (v) {
              return v !== -32767
            },
            zIndex: 300,
          }).addTo(this.map);
        });
      });
    }
  },

  mounted() {
    this.initMap();
    // this.ShowAscFile();
  },
}
</script>


<style scoped>
.container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

#mapTile {
  width: 100%;
  height: 100%;
  position: relative;
  outline: none;
  z-index: 1;
}
</style>
