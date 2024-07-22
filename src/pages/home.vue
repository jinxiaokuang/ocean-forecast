<template>
    <!-- <div class="container"> -->
      <div id="mapTile" style="background-color:#56AEF1;">

        <SeaIcon id="SeaIcon" v-on:updateSelectText="updateSelectText"></SeaIcon>

        <SeaTimeline id="seaTimeLine" v-on:updateSelectDate="updateSelectDate" ></SeaTimeline>
        <!-- <MapControls id="MapControls"></MapControls>  -->
        <div class="picker-content noselect">
    <span data-ref="content"><div class="p-title inlined" data-icon-after="">海浪</div><span class="block">周期 7 s.</span></span>
    <a class="picker-link iconfont tooltip-down hide-on-picker-drag" data-do="detail" data-tooltip="该地点的预报">?</a>
    <a class="picker-close-button hide-on-picker-drag" data-do="rqstClose,picker" data-icon=""></a>
</div>

        <div id="map-controls" class="map-controls">
          <svg t="1720862350081" class="icon" @click="zoomIn" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3148" width="39" height="22"><path d="M560.207 468.549l0-269.272c0-19.27-15.63-34.891-35.245-34.891l-24.163 0c-19.466 0-35.245 15.502-35.245 34.891l0 269.272-266.619 0c-19.08 0-34.548 15.786-34.548 34.512l0 26.571c0 19.06 15.35 34.512 34.548 34.512l266.619 0 0 260.417c0 19.36 15.63 35.055 35.245 35.055l24.163 0c19.465 0 35.245-15.886 35.245-35.055l0-260.417 257.854 0c19.17 0 34.71-15.786 34.71-34.512l0-26.572c0-19.06-15.729-34.512-34.71-34.512l-257.854 0z" fill="#ffffff" p-id="3149"></path>
          </svg>
          <svg t="1720862471486" class="icon" @click="zoomOut" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4170" width="30" height="20"><path d="M85.333333 512a64 64 0 0 1 64-64h725.333334a64 64 0 0 1 0 128h-725.333334A64 64 0 0 1 85.333333 512z" fill="#ffffff" p-id="4171"></path>
          </svg>
          <svg t="1720862506246" class="icon" @click="locateMe" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5198" width="37" height="21"><path d="M512 128C352 128 224 256 224 416c0 115.2 70.4 204.8 160 320 32 44.8 70.4 89.6 102.4 147.2C492.8 889.6 499.2 896 512 896l0 0c12.8 0 19.2-6.4 25.6-12.8 32-51.2 70.4-96 102.4-140.8 89.6-121.6 160-211.2 160-326.4C800 256 672 128 512 128zM512 512C460.8 512 416 473.6 416 416S454.4 320 512 320c51.2 0 96 38.4 96 96C608 467.2 569.6 512 512 512z" fill="none" p-id="5199"></path>
          </svg>
          <svg t="1720862548918" class="icon" @click="toggleFullScreen" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6287" width="42" height="22"><path d="M358.4 768H426.666667v85.333333H213.333333v-213.333333h85.333334v68.266667l128-128 59.733333 59.733333-128 128z m345.6 0l-128-128 59.733333-59.733333 132.266667 132.266666V640h85.333333v213.333333h-213.333333v-85.333333h64zM358.4 298.666667l128 128-59.733333 59.733333-128-128V426.666667H213.333333V213.333333h213.333334v85.333334H358.4z m345.6 0H640V213.333333h213.333333v213.333334h-85.333333V354.133333l-132.266667 132.266667-59.733333-59.733333 128-128z" fill="#ffffff" p-id="6288"></path>
          </svg>
          <svg t="1721202130951" class="icon" @click="downLoad" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2412" width="38" height="21"><path d="M552 586.178l60.268-78.53c13.45-17.526 38.56-20.83 56.085-7.38s20.829 38.56 7.38 56.085l-132 172c-16.012 20.863-47.454 20.863-63.465 0l-132-172c-13.45-17.526-10.146-42.636 7.38-56.085 17.525-13.45 42.635-10.146 56.084 7.38L472 586.177V152c0-22.091 17.909-40 40-40s40 17.909 40 40v434.178zM832 512c0-22.091 17.909-40 40-40s40 17.909 40 40v288c0 61.856-50.144 112-112 112H224c-61.856 0-112-50.144-112-112V512c0-22.091 17.909-40 40-40s40 17.909 40 40v288c0 17.673 14.327 32 32 32h576c17.673 0 32-14.327 32-32V512z" fill="#ffffff" p-id="2413"></path>
          </svg>
          <svg t="1720862634860" class="icon" @click="toggleMore" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7346" width="37" height="22"><path d="M512 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7347"></path><path d="M863 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7348"></path><path d="M161 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7349"></path>
          </svg>
        </div>
    </div>
</template>
  
<script>
import L from "leaflet";
import '../stores/leaflet.css';
import * as d3 from 'd3'
import SeaTimeline from "../components/SeaTimeline.vue";
import SeaIcon from "../components/icons/SeaIcon.vue";
import chroma from "chroma-js";
import screenfull from 'screenfull';
import { ElMessage } from 'element-plus'
// import 'leaflet.chinatmsproviders'
import 'leaflet-simple-map-screenshoter'
import '../stores/L.Control.Locate.min.js'
import '../stores/L.Control.Locate.min.css'

  
// 定义渐变颜色的存储对象数组 stops
var colorArray = [
    { position: 0.0, color: '#0D55FB' },
    { position: 0.3, color: 'lightblue' },
    { position: 0.6, color: 'lightgreen' },
    { position: 0.9, color: 'yellow' },
    { position: 1.2, color: 'rgb(213,174,51)' },
    { position: 1.5, color: '#EB4F34' },
    { position: 1.8, color: 'rgb(202,29,128)' },
  ];

// 定义基本颜色比例尺
var baseScale = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8];
// var baseItem = [
//   { factor: 'wave', base: '1.5', labelScale:baseScale * 1.5 / 1.8},
//   { factor: 'temp', base: '32', labelScale:baseScale * 32 / 1.8},
//   { factor: 'salinity', base: '36', labelScale:baseScale * 36 / 1.8},
//   { factor: 'current', base: '1', labelScale: baseScale * 1 / 1.8 },
//   { factor: 'wind', base: '1', labelScale: baseScale * 1 / 1.8 },
// ];

// 定义颜色条labelScale
var baseItem = [
  { factor: 'wave', base: '1.8', labelScale:[0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]},
  { factor: 'temp', base: '36', labelScale:[0, 6, 12, 18, 24, 30, 36]},
  { factor: 'salinity', base: '36', labelScale: [0, 6, 12, 18, 24, 30, 36] },
  { factor: 'current', base: '1.2', labelScale: [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]},
  { factor: 'wind', base: '12', labelScale: [0, 2, 4, 6, 8, 10, 12]},
];
// console.log(baseItem);

// 定义popup中海洋水文要素的单位
var baseUnit = [
  { factor: 'wave', text: '浪高', unit: 'm'},
  { factor: 'temp', text: '海温', unit: '℃'},
  { factor: 'salinity', text: '盐度', unit: '‰'},
  { factor: 'current', text: '海流', unit: 'm/s'},
  { factor: 'wind', text: '海风', unit: 'm/s'},  
]


export default {
    name: 'MapView',
    components: {
      SeaTimeline,
      // MapControls,
    },
    props: {

    },
    data() {
      return {
        // map: null,
        selectedDate: '' ,// 初始值
        color: '',
        scale: '',
        currentMagnitudeLayer: null, // 存储当前的magnitude图层引用
        currentAnimationLayer: null, // 存储粒子风场动画
        currentColorBar: null, // 颜色条
        popUp: null,
        time: '',
        text: 'wave',
        labelScale: '',
      }
    },

    methods: {
      initMap() {  //地图初始化
        this.map = L.map("mapTile", {
          center: [20, 125],
          zoom: 5,/*  */
          minZoom: 4,
          maxZoom: 7,
          zoomControl: false,  // 禁用 + - 按钮
          doubleClickZoom: false,  // 禁用双击放大
          attributionControl: false,  // 移除右下角 leaflet 标识
          // preferCanvas: true, 
        });

        // 地图的矢量图层（本地）
        const tile = L.tileLayer('/mapTile/{z}/{x}/{y}.png', {
          zIndex: 200,
        }).addTo(this.map);
        // const tile = L.tileLayer.chinaProvider(
        //   'GaoDe.Normal.Map',
        //   {
        //       key: 'e32465ca8c9815f2519fa19f6996059e',
        //       maxZoom:8,
        //       minZoom: 4,
        //       zIndex: 200,
        //   }).addTo(this.map);
  
        // 地图的标记图层
        const label = L.tileLayer(
            "https://t4.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=a8479c5bd1fd7b84c5a72669ed79a95b", {
              zIndex: 300,
            }
        ).addTo(this.map);
        
        // 版权信息attribution
        var attributionLink = '<a href="http://leafletjs.com" target="_blank">Leaflet</a> | © <a href="https://www.tianditu.gov.cn/" target="_blank">天地图</a> contributors';
        var attributionLayer = L.control.attribution({
          prefix: attributionLink,
          position: 'bottomright',
        }).addTo(this.map);  

        // 将矢量瓦片地图层与标签层置于顶部
        this.map.getPanes().overlayPane.appendChild(tile.getContainer());
        this.map.getPanes().overlayPane.appendChild(label.getContainer());   

        //添加定位元素
        var locateLayer = L.control.locate({
          locateOptions: {
            maxZoom: 7,
           }
         }
        ).addTo(this.map);


      },
    // 单独处理海风和海流（多了个Animation）
    processFileWindAndCurrent(uPath, vPath) {
        d3.text(uPath).then((u) => {
          d3.text(vPath).then((v) => {
            var vf = L.VectorField.fromASCIIGrids(u, v);

            // 不能放一起，会报地图元素冲突的错误，只能分开
            if (this.currentMagnitudeLayer) {
              this.map.removeLayer(this.currentMagnitudeLayer);
            }
            if (this.currentAnimationLayer) {
              this.map.removeLayer(this.currentAnimationLayer);
            }

            const s = vf.getScalarField('magnitude');
            // 海洋元素数值按一定的归一化
            var obj = baseItem.find(item => item.factor === this.text);
            s.grid = s.grid.map(row => { return row.map(x => x / obj.base * 1.8)});
            // 添加热力图层
            this.currentMagnitudeLayer = L.canvasLayer.scalarField(s, {
              color: this.color,
              opacity: 0.8,
              interpolate: true,
              inFilter: function (v) {
                return v !== 0
              },
              zIndex: 1,
            }).addTo(this.map);
            // this.map.fitBounds(this.currentMagnitudeLayer.getBounds());

            // 添加矢量动画图层
            let that = this; // 捕获 this 的值
            this.currentAnimationLayer = L.canvasLayer.vectorFieldAnim(vf, {
              paths: that.text === 'wind' ? 500 : 1000,
              width: 1,
              opacity: 1.0,
              color: 'white',
              velocityScale: that.text === 'wind' ? 1/20 : 1/10,
              inFilter: function (v) {
                return v !== 0
              },
              zIndex: 1,
            }).addTo(this.map);
            // this.map.fitBounds(this.currentAnimationLayer.getBounds());

            // 添加交互动画，点击区域获得经纬度与风速
          // let that = this; 
          this.currentAnimationLayer.on('click', function (e) {
            if (e.value !== null) {
              let lat = e.latlng.lat.toFixed(2).toString();
              let lng = e.latlng.lng.toFixed(2).toString();
              let vector = e.value;
              let v = vector.magnitude().toFixed(2);
              let d = vector.directionTo().toFixed(0);
              let unit = baseUnit.find(unit => unit.factor === that.text).unit;
              let text = baseUnit.find(unit => unit.factor === that.text).text;
              let html = (`<span>${text} ${v}${unit} to ${d}&deg<br>lat: ${lat}&deg lon: ${lng}&deg</span>`);
              // console.log(v, d);
              // console.log(that.map);
              let popup = L.popup()
                    .setLatLng(e.latlng)
                    .setContent(html)
                    .openOn(that.map);
              } 
            });


          });
        });
      },
      // 处理其他的海洋要素文件
      processFileOther(uPath) {
        d3.text(uPath).then((asc) => {
            // console.log(asc);

          var vf = L.ScalarField.fromASCIIGrid(asc);
          // console.log(vf);

          var obj = baseItem.find(item => item.factor === this.text);
          vf.grid = vf.grid.map(row => { return row.map(x => x / obj.base * 1.8) });

            // 如果当前已经有magnitude图层，先移除它
          if (this.currentMagnitudeLayer) {
            this.map.removeLayer(this.currentMagnitudeLayer);
          }
          if (this.currentAnimationLayer) {
            this.map.removeLayer(this.currentAnimationLayer);
            }
            this.currentMagnitudeLayer = L.canvasLayer.scalarField(vf, {
              color: this.color,
              opacity: 0.8,
              interpolate: true,
              inFilter: function (v) {
                return v !== 0
              },
              zIndex: 1,
            }).addTo(this.map);
          //  this.map.fitBounds(this.currentMagnitudeLayer.getBounds());

          // 点击区域获得经纬度与值
          let that = this; // 捕获 this 的值
          this.currentMagnitudeLayer.on('click', function (e) {
            if (e.value !== null) {
              let lat = e.latlng.lat.toFixed(2).toString();
              let lng = e.latlng.lng.toFixed(2).toString();
              let v = (e.value * obj.base / 1.8).toFixed(2).toString();
              console.log(that.text);
              let unit = baseUnit.find(unit => unit.factor === that.text).unit;
              let text = baseUnit.find(unit => unit.factor === that.text).text;
              let html = (`<span>${text} ${v}${unit}<br>lat: ${lat}&deg lon: ${lng}&deg</span>`);
              let popup = L.popup()
                    .setLatLng(e.latlng)
                    .setContent(html)
                    .openOn(that.map);
              } 
            });
           
          // // 添加控件图层
          // var controlLayer = L.control.layers({}, {
          //   // "Vector animation": animation,
          //   "Derived magnitude": magnitude,
          // }, {
          //   position: 'bottomright', // 放置在左下角
          //   collapsed: false
          // }).addTo(this.map);

          })
        },
      // 根据选择的日期更新数据
      updateSelectDate(e){   
        this.time = e.replace(/:/g, "-");
        // console.log('/ISAM/' + `${this.text}` + '_asc/' + `${this.text}-${this.time}` + '.asc');
        if (this.text === 'wind' || this.text === 'current') {
          console.log('/ISAM/' + `${this.text}` + 'u_asc/' + `${this.text}u-${this.time}` + '.asc');
          console.log('/ISAM/' + `${this.text}` + 'v_asc/' + `${this.text}v-${this.time}` + '.asc');

          this.processFileWindAndCurrent('/ISAM/' + `${this.text}` + 'u_asc/' + `${this.text}u-${this.time}` + '.asc', ('/ISAM/' + `${this.text}` + 'v_asc/' + `${this.text}v-${this.time}` + '.asc'));
        }
        else {
          this.processFileOther('/ISAM/' + `${this.text}` + '_asc/' + `${this.text}-${this.time}` + '.asc');
        }
      },
      // 根据选择的海洋要素更新数据
      updateSelectText(e) {
        this.text = e;

        // 更新colorBar的textLabel标签
        // this.currentColorBar.options.textLabels = baseItem.find(item => item.factor === this.text).labelScale;
        if (this.currentColorBar) {
          this.currentColorBar.remove();
          this.updateColorBar();
        }

        // console.log('/ISAM/' + `${this.text}` + '_asc/' + `${this.text}-${this.time}` + '.asc');
        if (this.text === 'wind' || this.text === 'current') {
          // console.log('/ISAM/' + `${this.text}` + 'u_asc/' + `${this.text}u-${this.time}` + '.asc');
          // console.log('/ISAM/' + `${this.text}` + 'v_asc/' + `${this.text}v-${this.time}` + '.asc');
          this.processFileWindAndCurrent('/ISAM/' + `${this.text}` + 'u_asc/' + `${this.text}u-${this.time}` + '.asc', ('/ISAM/' + `${this.text}` + 'v_asc/' + `${this.text}v-${this.time}` + '.asc'));
        }
        else {
          this.processFileOther('/ISAM/' + `${this.text}` + '_asc/' + `${this.text}-${this.time}` + '.asc');
        }
      },
      // 更新colorBar
      updateColorBar() {
        // 颜色条
        this.color = chroma.scale(colorArray.map(colors => colors.color)).domain(baseScale).mode('lch').gamma(2);
        // var color = chroma.scale(['blue','lightblue', 'lightgreen', 'yellow', 'rgb(213,174,51)','rgb(202,29,128)']).domain(range).mode('lch').gamma(2);
        // console.log(this.color);
        this.scale = [0.0, 1.8];

        this.currentColorBar = L.control.colorBar(this.color, this.scale, {
          // title: 'Currents surface velocity (m)',
          units: 'm',
          steps: 200,
          decimals: 2,
          width: 250,
          height: 20,

          position: 'topright',
          background: '#FFF',

          textColor: '#FFFFF',
          // textLabels: ['0', '0.3', '0.6', '0.9', '1.2', '1.5', '1.8'],
          textLabels: baseItem.find(item => item.factor === this.text).labelScale,
          labels: [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8],
          labelFontSize: 13,
        }).addTo(this.map);  
      },
      // 控制按钮组件响应
      // 放大区域
      zoomIn() {        
      if (this.map) {
        this.map.zoomIn();

        }
      },
      // 缩小区域
      zoomOut() {
        if (this.map) {
          this.map.zoomOut();
        }
      },
      // 获取用户定位
      locateMe() {
        // if (this.map && navigator.geolocation) {
        //   navigator.geolocation.getCurrentPosition(position => {
        //     const { latitude, longitude } = position.coords;
        //     const positionArr = [latitude, longitude];

        //     this.map.panTo(positionArr);
        //     // 添加定位图标并保存到状态
        //     // L.marker(positionArr).addTo(this.map);

        //     var marker = L.marker(positionArr, {
        //       icon: L.divIcon({
        //         iconSize: 32, // 根据你的需要设置大小
        //         className: 'leaflet-control-locate-location', // 自定义类名
        //         // html: '<div class="leaflet-control-locate-location circle"></div>' // 添加圆形元素
        //       })
        //     });
        //     // // 将动画类添加到标记点的圆形元素上
        //     // var circle = marker._icon.firstChild;
        //     // circle.classList.add('leaflet-control-locate-throb');
        //     // 添加到地图上
        //     marker.addTo(this.map);

        //   }, error => {
        //     console.error('获取位置时出错:', error);
        //   });
        // }
        // ElMessage({
        //   showClose: true,
        //   message: '获取位置成功！',
        //   type: 'success',
        // })
      },
      // 其他的东西（待定）
      toggleMore() {
        // 占位，以后的拓展功能
        ElMessage({
                    showClose: true,
                    message: '功能开发中！',
                    type: 'warning',
                  })
      },
      // 全屏/退出全屏
      toggleFullScreen() {
        // const container = document.getElementById('container');
        if (screenfull.isEnabled) {
		      screenfull.request();
	      } 
        else {
		      // Ignore or do something else
	      } 
      },
      // 截屏/保存地图图片
      downLoad(){
        // init plugin
        this.simpleMapScreenshoter = L.simpleMapScreenshoter({
          hidden: true, // hide screen btn on map
        }).addTo(this.map);
        this.simpleMapScreenshoter.takeScreen('blob', {
                    caption: function () {
                        return 'Hello world'
                    }
                }).then(blob => {
                  saveAs(blob, 'screen.png');
                  ElMessage({
                    showClose: true,
                    message: '保存图片成功！',
                    type: 'success',
                  })
                }).catch(e => {
                  alert(e.toString());
                })
        // listen on fired error or catch error in prev promise
        this.map.on('simpleMapScreenshoter.error', function (event) {
          var el = document.createElement('div');
          el.classList.add('create-screen-error');
          el.innerHTML = event.e.toString();
          document.getElementById('screens').appendChild(el);
        })                        
      },
    },
    // 组件生命周期
    mounted() {
      this.initMap();
      this.updateColorBar();
      // this.processFileWind('/ISAM/windu_asc/windu-2024-07-19T00-00-00.asc', '/ISAM/windv_asc/windv-2024-07-19T00-00-00.asc');

    },

  }

</script>

  
<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  margin: 0;
  padding: 0;
}

#mapTile {
  width: 100vw;
  height: 100vh;
  position: relative;
  outline: none;
  background-color: rgba(164, 205, 255, 1);

}

.icon-container {
  position: absolute;
  bottom: 540px;
  right: 5px;
  z-index: 499;
}

.map-controls {
  position: absolute;
  top: 70px;
  right: 10px;
  z-index: 500;
  background: rgba(93, 104, 111, 0.5);
  border-radius: 30px;

  width: 252px;
  height: 22px;
  box-shadow: 0 0 4px 0 rgb(21, 12, 0);
  display: flex;
  justify-content: space-evenly;
  /* 水平分散对齐 */
}

#map-controls svg {
  display: inline-block;
  margin: 0 px;
  padding: 5px 0px;
  cursor: pointer;
  background: none;
  border: none;

  position: relative;
  margin-top: -5px;
  z-index: 509;

}

#map-controls button i {
  pointer-events: none;
}

.tooltip-container {
  font-family: Arial, sans-serif;
  /* padding: 10px; */
  /* background-color: rgba(255, 255, 255, 0.903); */
  /* border: 1px solid #ccc; */
  border-radius: 5px;
  /* box-shadow: 2px 2px 10px rgba(0,0,0,0.2); */
  position: absolute;
  top: 200px;
  left: 200px;
  z-index: 1000;
  /* height: 200px;
  width: 200px; */
}

.flagpole {
  position: relative;
  height: 100px;
  width: 5px;
  left: -20px;
}

.text-container {
  display: flex;
  justify-content: space-around;
  /* 水平分散对齐 */
  align-items: center;
  /* 垂直居中对齐 */
  background-color: #d61a1aa5;
  /* 容器背景颜色 */
  padding: 10px;
  /* 容器内边距 */
  font-family: Arial, sans-serif;
  /* 字体 */
  z-index: 10000;
  position: absolute;
  top: 100px;
  right: 50px;
  height: 50px;
  width: 200px;
  color: hsl(0, 0%, 100%);
}

.flag-icon {
  background-color: #f8f5f500;
}





</style>