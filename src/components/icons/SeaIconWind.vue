<!-- SeawindIcon.vue -->
<template>
	<div @click="toggleActive">
		<span class="capsule-text">{{ text }}</span>
		<button class="icon-wind"
				:class="{ active: isActive }">
			<svg t="1720796579868" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="27064" width="200" height="200">
				<path d="M387.382347 651.26493a20.041418 20.041418 0 0 1 27.709086-5.558045l40.569671 27.14111a20.041418 20.041418 0 0 0 20.041417 1.298229l41.340495-20.731102a59.921404 59.921404 0 0 1 53.633105 0l44.220942 22.151041a19.960278 19.960278 0 0 0 17.931794 0l44.139803-22.151041a59.961974 59.961974 0 0 1 53.754814 0l44.139802 22.151041a19.960278 19.960278 0 0 0 17.931795 0l44.139802-22.151041a59.921404 59.921404 0 0 1 53.754814 0l41.299925 20.649963a19.879139 19.879139 0 0 0 20.041418-1.298229l40.569671-27.059971a20.041418 20.041418 0 0 1 22.19161 33.26713l-40.569671 27.14111a59.961974 59.961974 0 0 1-60.164823 3.73241l-41.299925-20.690532a19.960278 19.960278 0 0 0-17.931794 0l-44.139803 22.15104a59.921404 59.921404 0 0 1-53.754814 0l-44.139802-22.15104a20.000848 20.000848 0 0 0-17.931794 0l-44.139803 22.15104a59.921404 59.921404 0 0 1-53.754814 0l-44.139802-22.15104a19.960278 19.960278 0 0 0-17.931795 0l-41.340494 20.690532a60.245962 60.245962 0 0 1-60.164823-3.73241l-40.569671-27.14111a20.041418 20.041418 0 0 1-5.517475-27.709085z m0 95.987842a20.041418 20.041418 0 0 1 27.709086-5.558045l40.569671 27.14111a20.041418 20.041418 0 0 0 20.041417 1.298229l41.340495-20.731102a60.002544 60.002544 0 0 1 53.633105 0l44.220942 22.151041a20.284836 20.284836 0 0 0 17.931794 0l44.139803-22.151041a59.961974 59.961974 0 0 1 53.754814 0l44.139802 22.151041a20.284836 20.284836 0 0 0 17.931795 0l44.139802-22.151041a59.961974 59.961974 0 0 1 53.754814 0l41.299925 20.690532a19.879139 19.879139 0 0 0 20.041418-1.298229l40.569671-27.059971a20.041418 20.041418 0 0 1 22.19161 33.267131l-40.569671 27.14111a59.961974 59.961974 0 0 1-60.164823 3.732409l-41.299925-20.690532a19.960278 19.960278 0 0 0-17.931794 0l-44.139803 22.151041a60.043113 60.043113 0 0 1-53.754814 0l-44.139802-22.151041a20.000848 20.000848 0 0 0-17.931794 0l-44.139803 22.151041a60.043113 60.043113 0 0 1-53.754814 0l-44.139802-22.151041a19.960278 19.960278 0 0 0-17.931795 0l-41.340494 20.690532a60.245962 60.245962 0 0 1-60.164823-3.732409l-40.569671-27.14111a19.960278 19.960278 0 0 1-5.517475-27.709086z m27.709086 90.429796a20.041418 20.041418 0 0 0-22.19161 33.267131l40.569671 27.14111a60.083683 60.083683 0 0 0 60.164822 3.69184l41.259355-20.649963a19.960278 19.960278 0 0 1 17.931795 0l44.139802 22.151041a60.002544 60.002544 0 0 0 53.754814 0l44.139803-22.151041a20.041418 20.041418 0 0 1 17.931794 0l44.139802 22.151041a60.002544 60.002544 0 0 0 53.754814 0l44.139803-22.151041a19.960278 19.960278 0 0 1 17.931794 0l41.340495 20.649963a60.245962 60.245962 0 0 0 60.164822-3.69184l40.569671-27.14111a20.041418 20.041418 0 1 0-22.19161-33.267131l-40.569671 27.14111a20.000848 20.000848 0 0 1-20.041417 1.29823l-41.340495-20.731102a59.961974 59.961974 0 0 0-53.633105 0l-44.220942 22.15104a20.000848 20.000848 0 0 1-17.931794 0l-44.139803-22.15104a59.961974 59.961974 0 0 0-53.754814 0l-44.139802 22.15104a20.000848 20.000848 0 0 1-17.931794 0l-44.180372-22.15104a59.961974 59.961974 0 0 0-53.754814 0l-41.259356 20.690532a19.838569 19.838569 0 0 1-20.041417-1.25766z m0 0" p-id="27065"></path>
				<path d="M991.748738 196.925183S481.585124 46.208855 310.178263 1.460508a50.833798 50.833798 0 0 0-61.179064 36.512704l-247.474993 922.108054a51.84804 51.84804 0 0 0 34.808778 61.949888 51.888609 51.888609 0 0 0 63.978371-35.457893l106.941653-398.718727 791.83884-308.3295a44.626638 44.626638 0 0 0 24.341803-43.815245 44.626638 44.626638 0 0 0-31.847192-38.784606z m0 0" p-id="27066"></path>
			</svg>
		</button>
	</div>
</template>
  
<script>
export default {
  name: 'SeaIconWind',
  props: {
    activeText: String
  },
  data() {
    return {
      text: '海风',
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
      this.$emit('select', 'wind');
    }
  }
}
</script>
  
<style scoped>.capsule-text {
	padding: 5px 20px;
	background-color: #9198a1;
	color: #fefeff;
	border-radius: 20px;
	/* 胶囊形状的边框 */
	opacity: 1;
	font-weight: bold;
	cursor: pointer;
	position: relative;
	top: 170px;
	right: 50px;
	box-shadow: 0 0 4px 0 rgb(21, 12, 0);
}

.icon-wind,
.icon-wind *,
.icon-wind :after,
.icon-wind :before,
.icon-wind:after,
.icon-wind:before {
	border: 0 solid;
	box-sizing: border-box;
}

.icon-wind {
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

.icon-wind:disabled {
	cursor: default;
}

.icon-wind:-moz-focusring {
	outline: auto;
}

.icon-wind svg {
	vertical-align: middle;
}

.icon-wind [hidden] {
	display: none;
}

.icon-wind {
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

.icon-wind:hover {
	background: #0b99f7;
}

.icon-wind svg {
	--size: 18px;
	fill: #0b99f7;
	display: block;
	height: var(--size);
	left: calc(50% - var(--size) / 2);
	position: absolute;
	top: calc(50% - var(--size) / 2);
	width: var(--size);
}

.icon-wind:hover svg {
	fill: #FFFFFF;
}

.icon-wind:before {
	border: 5px solid #fff;
	border-radius: 50%;
	content: "";
	inset: 0.001px;
	opacity: 0;

	position: absolute;
	transform: scale(1.6);
	transition: 0.25s;
}

.icon-wind:hover:before {
	opacity: 1;
	transform: scale(1);
}

.icon-wind.active {
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

.icon-wind.active svg {
	fill: #FFFFFF;
}

</style>