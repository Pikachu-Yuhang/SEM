<template>
    <div id="echartMap" style="width: 700px; height: 500px"></div>
</template>
  
<script>
  import * as echarts from 'echarts';
  import '@/components/china.js';
  export default {
    name: 'echartsMap',
    components: {},
    props: {},
    data() {
      return {
        mapData: [],
      };
    },
    created() {
      this.$http.post("/tables/data", {
        'tablename': '远洋渔业',
        'kind': '境外出售量（吨）',
        'year': '2019'
      }).then((res) => {
        this.mapData = res.data;
        for (let row in this.mapData) {
           this.mapData[row].value = parseInt(this.mapData[row].value);
        }
        this.init();
      });
    },
    methods: {
      setMapData(data) {
        this.mapData = data;
      },
      init() {
        console.log(this.mapData);
        var option = {
          backgroundColor: '#FFFFFF',
          title: { text: '全国地图', subtext: '测试地图', x: 'center' },
          tooltip: { trigger: 'item' },
          grid: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
          },
          visualMap: {
            show: true,
            x: 'left',
            y: 'bottom',
            inRange:{
              color: ['#E0EAD5', '#18A0FB']
            },
          },
          series: [
            {
              name: '随机数据',
              type: 'map',
              map: 'china',
              roam: true,
              label: { show: false },
              emphasis: {
                label: { show: false },
                areaColor: 'red'
              },
              data: this.mapData,
            },
          ],
        };
        var chart = echarts.init(document.getElementById('echartMap'));
        chart.setOption(option);
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  