<!-- SeacurrentIcon.vue -->
<template>
	<div @click="toggleActive">
		<span class="capsule-text">{{ text }}</span>
		<button class="icon-current"
				:class="{ active: isActive }">
			<svg t="1721528701517" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2589" width="200" height="200">
				<path d="M0 201.44006l49.006232-104.436715c148.837953 107.393007 292.786653 107.393007 439.009424 0.227407C664.824684-32.3913 845.670188-32.3913 1023.331992 97.117049l-49.404195 104.209307c-147.075548-107.336156-290.057768-107.336156-436.280539-0.113703C360.838231 330.777853 179.253654 330.777853 0 201.44006z m0 362.486932L49.006232 459.376574c148.837953 107.449859 292.786653 107.449859 439.009424 0.227407 176.809027-129.5652 357.654531-129.5652 535.316336-0.113704l-49.404195 104.209308C826.852249 456.533985 683.926881 456.533985 537.647258 563.642733c-176.809027 129.622052-358.393604 129.622052-537.647258 0.284259z m0 362.43008l49.006232-104.436714c148.837953 107.449859 292.786653 107.449859 439.009424 0.227407 176.809027-129.622052 357.654531-129.622052 535.316336-0.113704l-49.404195 104.209308c-147.075548-107.279304-290.057768-107.279304-436.280539-0.113704-176.809027 129.622052-358.393604 129.622052-537.647258 0.227407z" p-id="2590"></path>
			</svg>
		</button>
	</div>
</template>
  
<script>
export default {
  name: 'SeaIconCurrent',
  props: {
    activeText: String
  },
  data() {
    return {
      text: '海流',
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
      this.$emit('select', 'current');
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

.icon-current,
.icon-current *,
.icon-current :after,
.icon-current :before,
.icon-current:after,
.icon-current:before {
  border: 0 solid;
  box-sizing: border-box;
}
.icon-current {
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
.icon-current:disabled {
  cursor: default;
}
.icon-current:-moz-focusring {
  outline: auto;
}
.icon-current svg {
  vertical-align: middle;
}
.icon-current [hidden] {
  display: none;
}
.icon-current {
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
.icon-current:hover {
  background: #0b99f7;
}
.icon-current svg {
  --size: 18px;
  fill: #0b99f7;
  display: block;
  height: var(--size);
  left: calc(50% - var(--size) / 2);
  position: absolute;
  top: calc(50% - var(--size) / 2);
  width: var(--size);
}
.icon-current:hover svg {
  fill: #FFFFFF;
}
.icon-current:before {
  border: 5px solid #fff;
  border-radius: 50%;
  content: "";
  inset: 0.001px;
  opacity: 0;

  position: absolute;
  transform: scale(1.6);
  transition: 0.25s;
}
.icon-current:hover:before {
  opacity: 1;
  transform: scale(1);
}

.icon-current.active {
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

.icon-current.active svg {
  fill: #FFFFFF;
}



</style>
  