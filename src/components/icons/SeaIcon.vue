<template>
  <div class="icon-container" >
    <SeaIconWave :active-text="activeText" @update:activeText="activeText = $event" @select="selectIcon"/>
    <SeaIconTemp :active-text="activeText" @update:activeText="activeText = $event" @select="selectIcon"/>
    <SeaIconSalinity :active-text="activeText" @update:activeText="activeText = $event" @select="selectIcon"/>
    <SeaIconCurrent :active-text="activeText" @update:activeText="activeText = $event" @select="selectIcon"/>
    <SeaIconWind :active-text="activeText" @update:activeText="activeText = $event" @select="selectIcon"/>
  </div>
</template>

<script>
import SeaIconTemp from './SeaIconTemp.vue';
import SeaIconSalinity from './SeaIconSalinity.vue';
import SeaIconWave from './SeaIconWave.vue';
import SeaIconWind from './SeaIconWind.vue';
import SeaIconCurrent from './SeaIconCurrent.vue';

export default {
  name: 'SeaIcon',
  components: {
    SeaIconTemp,
    SeaIconSalinity,
    SeaIconWave,
    SeaIconCurrent,
    SeaIconWind
  },
  data() {
    return {
      activeText: '海浪', // 初始时海浪组件被激活
      selectedText: 'wave', // 存储被选中的文本
    };
    },
    methods: {
    selectIcon(text) {
      this.selectedText = text;
      console.log('Selected:', this.selectedText);
      this.$emit('updateSelectText', `${this.selectedText}`);
    }
    },
    mounted() {
      // this.selectIcon(text); 
  }
}
</script>

<style scoped>
.icon-container {
	position: absolute;
	top: -40px !important;
	right: 5px;
	z-index: 8999;
}

</style>
