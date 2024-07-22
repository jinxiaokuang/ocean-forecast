<!-- SeasalinityIcon.vue -->
<template>
	<div @click="toggleActive">
		<span class="capsule-text">{{ text }}</span>
		<button class="icon-salinity"
				:class="{ active: isActive }">
			<!-- <svg t="1720796767796" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="29133" width="200" height="200"><path d="M556.842667 760.149333a42.666667 42.666667 0 1 1 0-85.333333 42.666667 42.666667 0 0 1 0 85.333333z m-42.666667-298.666666a42.666667 42.666667 0 1 1 0-85.333334 42.666667 42.666667 0 0 1 0 85.333334z m-170.666667 170.666666a42.666667 42.666667 0 1 1 0-85.333333 42.666667 42.666667 0 0 1 0 85.333333zM853.333333 213.333333V106.666667a21.333333 21.333333 0 0 1 21.333334-21.333334h42.666666a21.333333 21.333333 0 0 1 21.333334 21.333334v747.178666a85.333333 85.333333 0 0 1-85.333334 85.333334H213.376a85.333333 85.333333 0 0 1-85.333333-85.333334V220.373333l-40.533334-121.557333 60.714667-20.224a21.333333 21.333333 0 0 1 27.008 13.482667l30.464 91.306666a732.330667 732.330667 0 0 1 315.989333 9.898667c50.432 12.629333 104.106667 19.285333 160.981334 19.968v85.333333a779.946667 779.946667 0 0 1-181.717334-22.528 647.210667 647.210667 0 0 0-287.573333-7.253333v585.045333H853.333333V725.333333h-64a21.333333 21.333333 0 0 1-21.333333-21.333333v-42.666667a21.333333 21.333333 0 0 1 21.333333-21.333333H853.333333v-128h-106.666666a21.333333 21.333333 0 0 1-21.333334-21.333333v-42.666667a21.333333 21.333333 0 0 1 21.333334-21.333333H853.333333V298.666667h-64a21.333333 21.333333 0 0 1-21.333333-21.333334v-42.666666a21.333333 21.333333 0 0 1 21.333333-21.333334H853.333333z m-723.072 13.610667L128 213.418667v6.954666l2.218667 6.570667z" p-id="29134"></path></svg> -->
			<svg t="1720796829332" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="29687" width="200" height="200">
				<path d="M512 343.850667l19.712 23.850666c117.333333 141.824 176.554667 251.136 176.554667 331.392 0 122.154667-86.997333 222.506667-196.266667 222.506667s-196.266667-100.394667-196.266667-222.506667c0-80.256 59.221333-189.568 176.554667-331.392L512 343.850667z m0 80.682666l-2.304 2.901334C414.250667 547.285333 366.933333 638.762667 366.933333 699.093333c0 95.36 65.834667 171.306667 145.066667 171.306667s145.066667-75.946667 145.066667-171.306667c0-60.288-47.317333-151.808-142.762667-271.658666L512 424.533333zM234.666667 128.896l20.224 26.069333C329.258667 250.88 366.933333 325.077333 366.933333 380.714667c0 85.589333-57.898667 156.885333-132.266666 156.885333s-132.266667-71.253333-132.266667-156.885333c0-55.637333 37.674667-129.877333 112.042667-225.749334l20.224-26.069333z m0 84.309333l-4.565334 6.272C178.858667 290.602667 153.6 345.045333 153.6 380.714667c0 59.392 37.589333 105.685333 81.066667 105.685333s81.066667-46.293333 81.066666-105.685333c0-35.669333-25.258667-90.112-76.501333-161.237334L234.666667 213.205333zM793.6 170.666667a25.6 25.6 0 0 1 25.6 25.6v34.133333H896a25.6 25.6 0 0 1 0 51.2h-76.8v119.466667H896a25.6 25.6 0 0 1 0 51.2h-76.8v119.466666H896a25.6 25.6 0 0 1 0 51.2h-76.8v119.466667H896a25.6 25.6 0 0 1 0 51.2h-76.8v34.133333a25.6 25.6 0 0 1-51.2 0V196.266667a25.6 25.6 0 0 1 25.6-25.6z" p-id="29688"></path>
			</svg>
		</button>
	</div>
</template>
  
<script>
export default {
  name: 'SeaIconSalinity',
  props: {
    activeText: String
  },
  data() {
    return {
      text: '盐度',
    };
  },
  computed: {
    isActive() {
      // console.log(this.activeText === this.text);
      return this.activeText === this.text;
    }
  },
  methods: {
    toggleActive() {
      // console.log(this.activeText, this.text);
      this.$emit('update:activeText', this.text);
      this.$emit('select', 'salinity');
    }
  }
}
</script>

<style scoped>
.capsule-text {
  padding: 5px 20px;
  background-color: #9198a1;
  color: #fefeff;
  border-radius: 20px; /* 胶囊形状的边框 */
  opacity: 1;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  top: 170px;
  right: 50px;
  box-shadow: 0 0 4px 0 rgb(21, 12, 0);
}

.icon-salinity,
.icon-salinity *,
.icon-salinity :after,
.icon-salinity :before,
.icon-salinity:after,
.icon-salinity:before {
  border: 0 solid;
  box-sizing: border-box;
}
.icon-salinity {
  -webkit-tap-highlight-color: transparent;
  /* -webkit-appearance: button; */
  background-color: #ed0a0a;
  background-image: none;
  color: #50e81e;
  cursor: pointer;
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
    Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif,
    Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
  font-size: 100%;
  font-weight: 900;
  line-height: 1.5;
  margin: 0;
  /* -webkit-mask-image: -webkit-radial-gradient(#000, #fff); */
  text-transform: uppercase;
  box-shadow: 0 0 5px 0 rgba(58, 34, 2, 1);
}
.icon-salinity:disabled {
  cursor: default;
}
.icon-salinity:-moz-focusring {
  outline: auto;
}
.icon-salinity svg {
  vertical-align: middle;
}
.icon-salinity [hidden] {
  display: none;
}
.icon-salinity {
  background: #FFFFFF;
  background-clip: content-box;
  border-radius: 100%;
  box-sizing: border-box;
  display: block;
  height: 40px;
  /* -webkit-mask-image: none; */
  padding: 0;
  position: relative;
  top: 140px;
  transition: 0.2s;
  width: 40px;

}
.icon-salinity:hover {
  background: #0b99f7;
}
.icon-salinity svg {
  --size: 22px;
  fill: #0b99f7;
  display: block;
  height: var(--size);
  left: calc(50% - var(--size) / 2);
  position: absolute;
  top: calc(50% - var(--size) / 2);
  width: var(--size);
}
.icon-salinity:hover svg {
  fill: #FFFFFF;
}
.icon-salinity:before {
  border: 5px solid #fff;
  border-radius: 50%;
  content: "";
  inset: 0.001px;
  opacity: 0;

  position: absolute;
  transform: scale(1.6);
  transition: 0.2s;
}
.icon-salinity:hover:before {
  opacity: 1;
  transform: scale(1);
}

.icon-salinity.active {
  border: 5px solid #fff;
  border-radius: 50%;
  content: "";
  inset: 0.001px;
  opacity: 1;
  position: relative;
  top: 140px;
  transform: scale(1);
  background: #0b99f7;
  box-shadow: 0 0 5px 0 rgba(58, 34, 2, 1);
}

.icon-salinity.active svg {
  fill: #FFFFFF;
}
</style>
  