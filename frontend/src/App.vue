<template>
  <div>
    <NavBar />
    <SubNavBar />
    <MainBody />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import SubNavBar from "./components/SubNavBar.vue";
import MainBody from "./components/MainBody.vue";

export default {
  name: "App",
  components: {
    NavBar,
    SubNavBar,
    MainBody,
  },
};
</script>
