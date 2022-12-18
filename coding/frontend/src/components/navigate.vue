<template>
  <div id="total1">
    <div class="top">
      渔我所欲
    </div>
    <div class="nav">
      <ul>
        <li v-for="(item, i) in navChoice"
            class="navChoice"
            :class="{'currentChoice': i == current}"
            @click="changeNavChoice(i)"
            v-text="item">
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "navigate",
  data() {
    return {
      current: 0,
      navChoice: []
    }
  },
  created() {
    this.$http.get("/tables/sources")
        .then((res) => {
          this.navChoice = res.data.source_list;
        });
  },
  methods: {
    changeNavChoice(currentChoice) {
      this.current = currentChoice;
      this.$emit('changeCurrent', currentChoice, this.navChoice[currentChoice]);
    }
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

.navChoice {
  color: white;
  padding: 5px 20px;
  cursor: pointer;
  font-weight: 600;
  border-radius: 20px;
  transition: all 0.2s;
}

.currentChoice {
  color: #333333;
  background-color: rgba(255, 255, 255, 0.75);
}

</style>