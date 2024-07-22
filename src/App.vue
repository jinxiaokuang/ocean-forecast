<template>
  <div id="app">
    
    <!-- <Map msg="Welcome to Sea Forecast App"/> -->
    <router-view></router-view>
  </div>
</template>

<script>
import SeaTimeline from './components/SeaTimeline.vue';
import Map from './components/Map.vue'
import MapControls from './components/MapControls.vue';
import SeaIconWave from "./components/icons/SeaIconWave.vue"
import SeaIconTemp from './components/icons/SeaIconTemp.vue';
import SeaIconSalinity from './components/icons/SeaIconSalinity.vue';
import SeaIconWind from './components/icons/SeaIconWind.vue';
import SeaIconCurrent from "./components/icons/SeaIconCurrent.vue"
import SeaIcon from './components/icons/SeaIcon.vue';

export default {
  name: 'App',
  components: {
    Map,
    SeaTimeline,
    MapControls,
    SeaIconWave,
    SeaIconTemp,
    SeaIconSalinity,
    SeaIconWind,
    SeaIconCurrent,
    SeaIcon,
  },
  mounted() {
    document.title = 'Sea Forecast';
  }
}
</script>

<style>

body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  height: 100vh;
  width: 100vw;
}
</style>
<!--  -->