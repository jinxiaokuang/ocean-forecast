<template>
	<div class="seatimeline-container">
		<button @click="togglePlay" class="play-button">
			<svg v-if="!isPlaying" viewBox="0 0 24 24" class="play-icon">
				<polygon points="5,3 19,12 5,21"></polygon>
			</svg>
			<svg v-else viewBox="0 0 24 24" class="pause-icon">
				<rect x="5" y="4" width="4" height="16"></rect>
				<rect x="13" y="4" width="4" height="16"></rect>
			</svg>
		</button>
		<input
			   type="range"
			   min="0"
			   :max="(labels.length - 1) * 24"
			   step="1"
			   v-model="currentValue"
			   :style="{ background: sliderBackground }"
			   class="slider"
			   id="seatimelineSlider"
			   @input="updateDate"
			   @mousemove="showTooltip"
			   @mouseleave="hideTooltip"
			   @click="showClickTooltip">
		</input>
		<div id="verticalLines">
			<span
				  v-for="(label, index) in labels"
				  :key="'line' + index"
				  :class="{ 'vertical-line': true, 'midnight-line': index % 1 === 0 }"
				  :style="{ marginLeft: `calc((100% - 20px) / (labels.length - 1) * ${index})` }"></span>
		</div>
		<div id="seatimelineLabels">
			<span v-for="(label, index) in labels" :key="index" :style="{ left: `${index*112.12 - 6}px` }">{{ label }}</span>
		</div>
		<div v-if="tooltip.visible" :style="{ top: tooltip.top + 'px', left: tooltip.left + 'px'}" class="tooltip">
			{{ tooltip.content }}
		</div>
		<div v-if="playTooltip.visible" :style="{ top: playTooltip.top + 'px', left: playTooltip.left + 'px'}" class="tooltip">
			{{ playTooltip.content }}
		</div>
		<!-- 当前时间指示 -->
		<svg viewBox="0 0 24 24" class="now-time-icon" :style="{left: nowTimeIndex.left + 'px'}">
			<rect x="15" y="4" width="3" height="7"></rect>
		</svg>
	</div>
</template>

<script>

import { ElMessage } from 'element-plus'
import 'element-plus/es/components/message/style/css'
// import { months } from 'moment';

export default {
  name: "SeaTimeline",
  data() {
    return {
      labels: [],
      dates: [{
        year: "",
        month: "",
        day: "",
        hour: "",
        week: "",
      }], 
      // 标注日期数组
      tooltip: {
        visible: false,
        content: "",
        top: 0,
        left: 0,
      },
      playTooltip: {
        visible: false,
        content: "",
        top: 0,
        left: 0,
      },
      nowTimeIndex: {
        left: 0,
      },
      currentValue: 0,
      isPlaying: false,
      playInterval: null,
      selectDate: "",
    };
  },
  computed: {
    sliderBackground() {
      const percentage = (this.currentValue / ((this.labels.length - 1) * 24)) * 100;
      return `linear-gradient(to right, rgb(2, 185, 252) ${percentage}%, #8d8d94 ${percentage}%)`;
    }
  },
  methods: {
    updateDate() {
      // 更新时间和弹窗
      this.showPlayTooltip();
    },
    showTooltip(event) {
      const sliderWidth = this.$el.querySelector('.slider').clientWidth;
      const position = event ? event.offsetX / sliderWidth : this.currentValue / ((this.labels.length - 1) * 24);
      const totalHours = (this.labels.length - 1) * 24;
      const value = Math.floor(position * totalHours);
      const dayIndex = Math.floor(value / 24);
      let hour = value % 24;
      hour = String(hour).padStart(2, '0'); 
      const date = this.labels[dayIndex];
      this.tooltip.content = `${date} ${hour}:00`;
      if (event) {
        this.tooltip.top = event.clientY - 40;
        this.tooltip.left = event.clientX - 200;
      } else {
        const slider = this.$el.querySelector('.slider');
        const sliderRect = slider.getBoundingClientRect();
        this.tooltip.top = sliderRect.top - 40;
        this.tooltip.left = sliderRect.left + position * sliderRect.width - 200;
        // console.log(this.tooltip.left);
      }
      this.tooltip.visible = true;
    },
    hideTooltip() {
      this.tooltip.visible = false;
    },
    showClickTooltip(event) {
      this.showTooltip(event);
    },
    showPlayTooltip() {
      const slider = this.$el.querySelector('.slider');
      const sliderRect = slider.getBoundingClientRect();
      const position = this.currentValue / ((this.labels.length - 1) * 24);
      this.playTooltip.top = sliderRect.top - 40;
      this.playTooltip.left = sliderRect.left + position * sliderRect.width - 200;
      const value = this.currentValue;
      const dayIndex = Math.floor(value / 24 +1);

      this.dates[dayIndex].hour = String(value % 24).padStart(2, '0'); 
      // console.log(this.dates.hour);

      this.playTooltip.content = `${this.dates[dayIndex].month}-${this.dates[dayIndex].day} ${this.dates[dayIndex].week} ${this.dates[dayIndex].hour}:00`;
      this.playTooltip.visible = true;

      // 2023-01-01T00:00:00 返回时间案例
      this.selectDate = `${this.dates[dayIndex].year}-${this.dates[dayIndex].month}-${this.dates[dayIndex].day}T${this.dates[dayIndex].hour}:00:00`;
      console.log("selectDate:" + this.selectDate);

      // 有缺陷，没有考虑年和闰月，但不需要
      const today = new Date();
      const lim = (parseInt(this.dates[dayIndex].month) - parseInt(today.getMonth()+1)) * 30 * 24 + (parseInt(this.dates[dayIndex].day) - parseInt(today.getDate())) * 24 + parseInt(this.dates[dayIndex].hour) - parseInt(today.getHours());
      if (lim > 72) {
        ElMessage({
          showClose: true,
          message: '选择预报时间超过72小时，请重新选择！',
          type: 'error',
        })
      }
      else {
        this.$emit('updateSelectDate', `${this.selectDate}`);
      }
    },
    generateLabels() {
      const today = new Date();
      const dayOfWeek = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];

      for (let i = 0; i < 11; i++) {
        const date = new Date(today);
        date.setDate(date.getDate() + i);
        // 获取当前日期的年月日
        var nowYear = date.getFullYear();
        var nowMonth = String(date.getMonth() + 1).padStart(2, '0');
        var nowDay = String(date.getDate()).padStart(2, '0');
        var nowWeek = dayOfWeek[date.getDay()];
        var nowHour = String(date.getHours()).padStart(2, '0');
        // 创建一个新的对象，并赋值
        let dateObject = {
          year: nowYear,
          month: nowMonth,
          day: nowDay,
          hour: nowHour,
          week: nowWeek,
        }
        this.currentValue = parseInt(nowHour);
        // console.log(dateObject);
        if(i < 10){
          this.dates.push(dateObject);
          this.labels.push(`${nowMonth}-${nowDay} ${nowWeek}`)
        }
        else{
          this.labels.push(`  `);
        }
      }

      const sliderT = this.$el.querySelector('.slider');
      const sliderRectT = sliderT.getBoundingClientRect();
      const positionT = parseInt(today.getHours()) / ((this.labels.length - 1) * 24);
      // console.log(positionT);
      this.nowTimeIndex.left = sliderRectT.left + positionT * sliderRectT.width - 800;
      // console.log(this.nowTimeIndex.left);

    },
    togglePlay() {
      if (this.isPlaying) {
        clearInterval(this.playInterval);
      } else {
        this.playInterval = setInterval(() => {
          if (this.currentValue < (this.labels.length - 1) * 24) {
            this.currentValue++;
          } else {
            const date = new Date(today);
            this.currentValue = String(date.getHours()).padStart(2, '0'); // 循环播放
          }
          this.updateDate();
        }, 1000); // 每秒移动一个小时
      }
      this.isPlaying = !this.isPlaying;
      if (!this.isPlaying) {
        this.showPlayTooltip();
      }
    },

  },
  mounted() {
    this.generateLabels(); // 初始化生成标注日期数组

    // 每天更新一次标注
    setInterval(() => {
      this.labels = []; // 清空原有标注
      this.generateLabels(); // 重新生成标注
    }, 24 * 60 * 60 * 1000); // 每24小时更新一次

    // 更新显示弹窗
    this.updateDate();
  },
};
</script>


<style>.seatimeline-container {
	width: 80%;
	height: 30px;
	margin: 5px auto;
	text-align: center;
	position: absolute;
	bottom: 25px;
	left: 180px;

	z-index: 9000;
	/* 确保它在最上层 */
	/* background-color: #f6f8f9d8; */
	opacity: 1 !important;

	/* border: 2px solid #85b2ebd8; */
	padding: 5px;
	border-radius: 10px;
	/* box-shadow: 0 0 2px 0 rgba(32, 75, 119, 0.8); */
}

.slider {
	width: 100%;
	-webkit-appearance: none;
	appearance: none;
	position: relative;
	bottom: 31px;
	height: 7px;
	outline: none;
	opacity: 0.9 !important;
	transition: opacity 0.2s;
	z-index: 9999;
	cursor: pointer;
	border-radius: 10px;
	box-shadow: 0 0 2px 0 rgba(32, 75, 119, 0.8);
	background: linear-gradient(to right, white 0%, white calc(100% / (labels.length - 1) * currentValue / ((labels.length - 1) * 24)), black calc(100% / (labels.length - 1) * currentValue / ((labels.length - 1) * 24)), black 100%);

}

.slider:hover {
	opacity: 1;
}

.slider::-webkit-slider-thumb {
	-webkit-appearance: none;
	appearance: none;
	width: 3px;
	height: 6px;
	background: #4CAF50;
	cursor: hand;
	border-radius: 50%;
	transition: width 0.2s, height 0.2s;
}

.slider::-webkit-slider-thumb:hover {
	width: 0px;
	height: 12px;
}

.slider::-moz-range-thumb {
	width: 8px;
	height: 8px;
	background: #4CAF50;
	cursor: hand;
	border-radius: 50%;
	transition: width 0.2s, height 0.2s;
}

.slider::-moz-range-thumb:hover {
	width: 12px;
	height: 12px;
}

#seatimelineLabels {
	position: relative;
	bottom: 32px;
	margin-top: -20px;
	height: 10px;
	/* 设置标签容器的高度以便定位 */
	right: -20px;
	display: flex;
	opacity: 1;
	color: hsl(0, 0%, 100%);
	z-index: 9999;
	/* justify-content: space-between;  */
}

#seatimelineLabels span {
	margin-right: -48px;
	/* 调整标签之间的间距 */
	font-size: 12px;
	/* 设置字体大小，可以根据需要调整 */
	position: relative;
}

#verticalLines {
	display: flex;
	justify-content: space-between;
	position: relative;
	bottom: 36px;
	/* 调整以对齐时间标注 */
	right: -1px;

}

.vertical-line {
	height: 15px;
	border-left: 2px solid rgb(248, 245, 245);
	text-align: center;
}

.midnight-line {
	border-color: rgb(249, 247, 247);
	/* 添加颜色以区分0点位置 */
}

.tooltip {
	position: absolute;
	top: -25px !important;
	background: rgb(254, 142, 31);
	border: 1px solid #f0a177;
	padding: 5px;
	border-radius: 6px;

	color: rgb(244, 248, 248);
	box-shadow: 0 0 4px 0 rgba(58, 34, 2, 0.8);
	opacity: 0.8 !important;
	font-family: Microsoft YaHei;

}

.tooltip::after {
	content: "";
	position: absolute;
	left: 12px;
	top: 100%;
	border-top: 8px solid rgb(254, 142, 31);
	border-left: 8px solid transparent;
	border-right: 8px solid transparent;
	opacity: 1.0 !important;
}

.play-button {
	position: relative;
	top: -3.6px;
	left: -650px;
	z-index: 9999;
	/* 确保它在最上层 */
	padding: 2px;
	background: white;
	color: rgb(205, 38, 38);
	border: none;
	border-radius: 100%;
	box-shadow: 0 0 5px 0 rgba(58, 34, 2, 1);
	cursor: pointer;
	font-size: 20px;
	height: 35px;
	width: 35px;
}

.play-button::before {
	border: 5px solid #fff;
	border-radius: 50%;
	content: "";
	inset: 0.001px;
	opacity: 0;

	position: absolute;
	transform: scale(1.5);
	transition: 0.2s;
}

.play-button:hover:before {
	opacity: 1;
	transform: scale(1);
}

.play-icon,
.pause-icon {
	position: relative;
	top: 2.2px;
	left: 1.3px;
	width: 25px;
	height: 25px;
	fill: rgb(205, 38, 38);
}

.play-icon polygon {
	transition: all 0.3s ease-in-out;
}

.pause-icon rect {
	transition: all 0.3s ease-in-out;
}

.now-time-icon {
	position: relative;
	top: -53px;

	width: 25px;
	height: 25px;
	fill: rgb(255, 29, 29);
	z-index: 9999;
}

</style>