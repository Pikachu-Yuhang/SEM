<template>
    <div id="echartMap" style="width: 700px; height: 600px"></div>
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
        max: 0
      };
    },
    methods: {
      init(mapData, tableName, tableSubName, max) {
        this.mapData = mapData;
        this.mapData.sort(function (a, b) {
          return a.value - b.value;
        });
        this.max = max;
        var chart = echarts.init(document.getElementById('echartMap'));

        var mapOption = {
          backgroundColor: '#FFFFFF',
          title: { text: tableName, subtext: tableSubName, x: 'center' },
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
            max: this.max,
            inRange:{
              color: ['#E0EAD5', '#18A0FB']
            },
          },
          animationDurationUpdate: 1000,
          series: [
            {
              name: tableName,
              type: 'map',
              map: 'china',
              roam: true,
              label: { show: false },
              emphasis: {
                label: { show: false },
              },
              data: this.mapData,
              universalTransition: true,
            },
          ],
          toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
              restore: {},
              saveAsImage: {},
              myTool: {
                title: "切换视图",
                show: true,
                icon: "path://M1131.861333 0H512a512 512 0 0 0 0 1024h619.861333a512 512 0 0 0 0-1024z m0 887.466667H512a375.466667 375.466667 0 0 1 0-750.933334h619.861333a375.466667 375.466667 0 0 1 0 750.933334z",
                onclick: function() {
                  chart.setOption(barOption, true);
                }
              }
            }
          }
        };

        const barOption = {
          title: {
            text: '我国各省2021年渔业总产值（单位：亿元）',
            x: "center",
            textStyle: {
              fontSize: 18,
              color: "black"
            },
          },
          xAxis: {
            type: 'value'
          },
          yAxis: {
            type: 'category',
            axisLabel: {
              rotate: 30
            },
            data: this.mapData.map(function (item) {
              return item.name;
            })
          },
          visualMap: {
            orient: 'horizontal',
            left: 'center',
            text: ['High', 'Low'],
            max: 1800,
            min: 0,
            dimension: 0,
            inRange: {
              color: ['#E0EAD5', '#18A0FB']
            }
          },
          tooltip:{
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              crossStyle: {
                color: '#999'
              }
            }
          },
          itemStyle:{
            emphasis:{
              focus: 'self'
            }
          },
          animationDurationUpdate: 1000,
          series: {
            type: 'bar',
            id: '渔业总产值',
            mapType: 'china',
            data: this.mapData.map(function (item) {
              return item.value;
            }),
            universalTransition: true
          },
          toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
              restore: {},
              saveAsImage: {},
              myTool: {
                title: "切换视图",
                show: true,
                icon: "path://M1131.861333 0H512a512 512 0 0 0 0 1024h619.861333a512 512 0 0 0 0-1024z m0 887.466667H512a375.466667 375.466667 0 0 1 0-750.933334h619.861333a375.466667 375.466667 0 0 1 0 750.933334z",
                onclick: function() {
                  chart.setOption(mapOption, true);
                }
              }
            }
          }
        };

        chart.setOption(mapOption);
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  