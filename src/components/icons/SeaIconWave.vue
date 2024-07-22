<!-- SeaWaveIcon.vue -->
<template>
	<div @click="toggleActive">
		<span class="capsule-text">{{ text }}</span>
		<button class="icon-wave"
				:class="{ active: isActive }">
			<svg t="1720784180242" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5016" width="200" height="200">
				<path d="M402.563723 1021.887435h-6.389321c-9.047277 3.066874-8.689476 2.555728 6.389321 0zM564.596884 9.052389C433.79472-11.393436 356.662846 6.394432 323.591724 26.840257c-65.426639 32.559976-100.286771 83.47008-100.28677 156.257216 0 80.761008 71.458158 146.44322 159.733006 146.44322 9.200621 0 17.890097-0.715604 26.681801-2.044583-46.309793-14.414306-63.126484-74.116115-63.126484-92.875159 0-44.571898 20.496939-89.8594 80.147634-102.842499 0 0 47.894345-15.998858 135.811391 7.973872 124.157271 46.923168 160.44861 102.944728 193.979763 188.663848 41.913941 135.402475 6.440435 315.683535-60.417413 418.014888-127.530832 195.257627-443.009909 258.639684-443.009909 258.639684 320.488304-78.716425 463.813536-264.262286 492.182118-504.142925 18.554586-318.239263-279.801112-393.428784-326.366478-196.433262 41.402795-36.649141 86.639183-28.879728 131.87557-10.018454 104.018134 71.918189 89.29714 185.596975 79.89206 248.110084-21.212543 140.973962-104.018134 277.654301-225.824135 360.817693-127.990863 72.633793-296.46446 105.807143-352.946051 118.585784h344.30769c28.57304-1.686781 151.656905-9.609538 217.748034-34.246756C793.999039 920.476144 972.031058 759.516388 972.031058 499.087695 972.031058 238.454543 771.406402 41.459021 564.54577 9.001274z m-343.08094 907.283476c-37.466974 29.748675-166.122327 87.405901-166.122326 87.405901s119.250273-10.836287 215.959024-52.750228c86.741412-37.518089 127.581947-76.467385 168.166909-136.57811 36.955828-54.692581 72.122647-222.348345-58.679517-302.393749-76.058468-46.514251-181.967841-47.536543-225.721906 8.996163-51.932395 67.11342-11.756349 125.690708-11.756349 125.690708s15.487712-53.67029 66.44893-62.870911c13.647588-2.555728 66.346701 0.56226 93.897451 25.65951 20.752512 18.861273 53.976977 52.647999 35.217933 138.724921-14.107619 65.119952-51.421249 115.621139-117.410149 168.166909z" p-id="5017"></path>
			</svg>

		</button>
	</div>
</template>
  
<script>
export default {
  name: 'SeaIconWave',
  props: {
    activeText: String
  },
  data() {
    return {
      text: '海浪',
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
      this.$emit('select', 'wave');
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

.icon-wave,
.icon-wave *,
.icon-wave :after,
.icon-wave :before,
.icon-wave:after,
.icon-wave:before {
  border: 0 solid;
  box-sizing: border-box;
}
.icon-wave {
  -webkit-tap-highlight-color: transparent;
  /* -webkit-appearance: button; */
  background-color: #ed0a0a;
  background-image: none;
  color: #0b99f7;
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
.icon-wave:disabled {
  cursor: default;
}
.icon-wave:-moz-focusring {
  outline: auto;
}
.icon-wave svg {
  vertical-align: middle;
}
.icon-wave [hidden] {
  display: none;
}
.icon-wave {
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
  transition: 0.25s;
  width: 40px;

}
.icon-wave:hover {
  background: #0b99f7;
}
.icon-wave svg {
  --size: 20px;
  fill: #0b99f7;
  display: block;
  height: var(--size);
  left: calc(50% - var(--size) / 2);
  position: absolute;
  top: calc(50% - var(--size) / 2);
  width: var(--size);
}
.icon-wave:hover svg {
  fill: #FFFFFF;
}
.icon-wave:before {
  /* 光圈 */
  border: 5px solid #fff;
  border-radius: 50%;
  content: "";
  inset: 0.001px;
  opacity: 0;

  position: absolute;
  transform: scale(1.6);
  transition: 0.2s;
}
.icon-wave:hover:before {
  opacity: 1;
  transform: scale(1);
}

.icon-wave.active {
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

.icon-wave.active svg {
  fill: #FFFFFF;
}

</style>
  