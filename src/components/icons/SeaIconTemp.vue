<!-- SeatempIcon.vue -->
<template>
	<div @click="toggleActive">
		<span class="capsule-text">{{ text }}</span>
		<button class="icon-temp"
				:class="{ active: isActive }">
			<svg t="1720794648727" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="11150" width="200" height="200">
				<path d="M604.672 563.2v-23.04h77.824v23.04h-77.824z m0-74.24h77.824v24.576h-77.824v-24.576z m0-49.152h77.824v24.576h-77.824v-24.576z m0-51.2h77.824v24.576l-77.824-1.536v-23.04z m0-52.736h77.824v26.112h-77.824v-26.112z m0-49.152h77.824v24.576h-77.824V286.72z m45.056 433.664c0 82.432-66.56 148.992-148.992 148.992s-148.992-66.56-148.992-148.992c-0.512-54.272 28.672-103.936 76.288-130.048V260.096c1.024-41.472 34.816-74.24 76.288-74.24 40.96 0 74.24 32.768 74.752 73.728V593.92c43.52 27.136 70.656 74.752 70.656 126.464zM553.472 609.28V260.096c-0.512-27.648-23.552-49.152-50.688-48.64-26.624 0.512-48.128 22.016-48.64 48.64v345.6c-64 25.6-94.72 98.304-69.12 161.792 25.6 64 98.304 94.72 161.792 69.12 64-25.6 94.72-98.304 69.12-161.792-11.264-28.672-33.792-52.224-62.464-65.536z m-52.736 209.92c-54.784 0.512-98.816-43.52-99.328-98.304 0-46.592 32.256-87.04 77.824-97.28v-235.52h49.664v237.568c52.224 14.848 82.944 69.632 67.584 121.856-12.288 43.008-51.2 72.192-95.744 71.68z" p-id="11151"></path>
			</svg>
		</button>
	</div>
</template>
  
<script>
export default {
  name: 'SeaIconTemp',
  props: {
    activeText: String
  },
  data() {
    return {
      text: '海温',
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
      this.$emit('select', 'temp');
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

.icon-temp,
.icon-temp *,
.icon-temp :after,
.icon-temp :before,
.icon-temp:after,
.icon-temp:before {
  border: 0 solid;
  box-sizing: border-box;
}
.icon-temp {
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
.icon-temp:disabled {
  cursor: default;
}
.icon-temp:-moz-focusring {
  outline: auto;
}
.icon-temp svg {
  vertical-align: middle;
}
.icon-temp [hidden] {
  display: none;
}
.icon-temp {
  background: #FFFFFF;
  background-clip: content-box;
  border-radius: 100%;
  box-sizing: border-box;
  display: block;
  height: 40px;
  padding: 0;
  position: relative;
  top: 140px;
  transition: 0.2s;
  width: 40px;

}
.icon-temp:hover {
  background: #0b99f7;
}
.icon-temp svg {
  --size: 35px;
  fill: #0b99f7;
  display: block;
  height: var(--size);
  left: calc(50% - var(--size) / 2);
  position: absolute;
  top: calc(50% - var(--size) / 2);
  width: var(--size);
}
.icon-temp:hover svg {
  fill: #FFFFFF;
}
.icon-temp:before {
  border: 5px solid #fff;
  border-radius: 50%;
  content: "";
  inset: 0.001px;
  opacity: 0;

  position: absolute;
  transform: scale(1.6);
  transition: 0.2s;
}
.icon-temp:hover:before {
  opacity: 1;
  transform: scale(1);
}

.icon-temp.active {
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

.icon-temp.active svg {
  fill: #FFFFFF;
}

</style>
  