<template>
  <div id="map-controls" class="map-controls">
    <svg t="1720862350081" class="icon" @click="zoomIn" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3148" width="23" height="22"><path d="M560.207 468.549l0-269.272c0-19.27-15.63-34.891-35.245-34.891l-24.163 0c-19.466 0-35.245 15.502-35.245 34.891l0 269.272-266.619 0c-19.08 0-34.548 15.786-34.548 34.512l0 26.571c0 19.06 15.35 34.512 34.548 34.512l266.619 0 0 260.417c0 19.36 15.63 35.055 35.245 35.055l24.163 0c19.465 0 35.245-15.886 35.245-35.055l0-260.417 257.854 0c19.17 0 34.71-15.786 34.71-34.512l0-26.572c0-19.06-15.729-34.512-34.71-34.512l-257.854 0z" fill="#ffffff" p-id="3149"></path>
    </svg>
    <svg t="1720862471486" class="icon" @click="zoomOut" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4170" width="19" height="21"><path d="M85.333333 512a64 64 0 0 1 64-64h725.333334a64 64 0 0 1 0 128h-725.333334A64 64 0 0 1 85.333333 512z" fill="#ffffff" p-id="4171"></path>
    </svg>
    <svg t="1720862506246" class="icon" @click="locateMe" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5198" width="29" height="21"><path d="M512 128C352 128 224 256 224 416c0 115.2 70.4 204.8 160 320 32 44.8 70.4 89.6 102.4 147.2C492.8 889.6 499.2 896 512 896l0 0c12.8 0 19.2-6.4 25.6-12.8 32-51.2 70.4-96 102.4-140.8 89.6-121.6 160-211.2 160-326.4C800 256 672 128 512 128zM512 512C460.8 512 416 473.6 416 416S454.4 320 512 320c51.2 0 96 38.4 96 96C608 467.2 569.6 512 512 512z" fill="#ffffff" p-id="5199"></path>
    </svg>
    <svg t="1720862548918" class="icon" @click="toggleFullScreen" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6287" width="27" height="21"><path d="M358.4 768H426.666667v85.333333H213.333333v-213.333333h85.333334v68.266667l128-128 59.733333 59.733333-128 128z m345.6 0l-128-128 59.733333-59.733333 132.266667 132.266666V640h85.333333v213.333333h-213.333333v-85.333333h64zM358.4 298.666667l128 128-59.733333 59.733333-128-128V426.666667H213.333333V213.333333h213.333334v85.333334H358.4z m345.6 0H640V213.333333h213.333333v213.333334h-85.333333V354.133333l-132.266667 132.266667-59.733333-59.733333 128-128z" fill="#ffffff" p-id="6288"></path>
    </svg>
    <svg t="1720862634860" class="icon" @click="toggleMenu" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7346" width="21" height="20"><path d="M512 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7347"></path><path d="M863 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7348"></path><path d="M161 512m-96.7 0a96.7 96.7 0 1 0 193.4 0 96.7 96.7 0 1 0-193.4 0Z" fill="#ffffff" p-id="7349"></path>
    </svg>
  </div>
</template>

<script>
export default {
  name: "MapControls",
  props: {
    map: {
      type: Object,   // 参数获取暂存
      required: true
    },
    AMap: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      marker: null // 新增的状态变量
    }
  },
  methods: {
    zoomIn() {        
      if (this.map) {
        this.map.zoomIn();

      }
    },
    zoomOut() {
      if (this.map) {
        this.map.zoomOut();
      }
    },
    locateMe() {
      if (this.map && navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          const { latitude, longitude } = position.coords;
          const positionArr = [longitude, latitude];

          this.map.setCenter(positionArr);

          // 添加定位图标并保存到状态
          this.marker = new this.AMap.Marker({
            position: positionArr,
            map: this.map,
            icon: new this.AMap.Icon({
              size: new this.AMap.Size(102, 102),  // 图标大小
              image: 'https://webapi.amap.com/theme/v1.3/markers/n/mark_b.png', // 图标地址，可以替换为自己的图标
              imageSize: new this.AMap.Size(22, 32)
            })
          });
        }, error => {
          console.error('获取位置时出错:', error);
        });
      }
    },
    toggleMenu() {
      const menu = document.getElementById('menu');
      if (menu) {
        menu.style.display = (menu.style.display === 'none' || !menu.style.display) ? 'block' : 'none';
      }
    },
    toggleFullScreen() {
      const container = document.getElementById('container');
      if (!document.fullscreenElement) {
        if (container.requestFullscreen) {
          container.requestFullscreen();
        } else if (container.mozRequestFullScreen) { /* Firefox */
          container.mozRequestFullScreen();
        } else if (container.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
          container.webkitRequestFullscreen();
        } else if (container.msRequestFullscreen) { /* IE/Edge */
          container.msRequestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.mozCancelFullScreen) { /* Firefox */
          document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) { /* Chrome, Safari and Opera */
          document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) { /* IE/Edge */
          document.msExitFullscreen();
        }
      }
    }
  },
  mounted() {
    this.zoomIn();
    this.zoomIn();
  }
}
</script>


<style>
.map-controls {
  position: absolute;
  top: 70px;
  right: 10px;
  z-index: 9000;
  background: rgba(93, 104, 111, 0.5);
  border-radius: 30px;
  
  width: 252px;
  height: 22px;
  box-shadow: 0 0 4px 0 rgb(21, 12, 0);
  display: flex;
  justify-content: space-around; /* 水平分散对齐 */
}

#map-controls svg {
  display: inline-block;
  margin: 5 5px;
  padding: 5px 10px;
  cursor: pointer;
  background: none;
  border: none;
  font-size: 20px;
  z-index: 9999;
  cursor: pointer;
}

#map-controls button i {
  pointer-events: none;
}
</style>
