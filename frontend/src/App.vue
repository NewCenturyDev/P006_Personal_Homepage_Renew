<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  async beforeMount() {
    try {
      await this.$store.dispatch('getProfile');
      await this.$store.dispatch('getActivity');
    } catch (error) {
      alert(error);
    }
  }
}
</script>

<style lang="scss">
body {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
