<template>
  <div class="bg-white text-black py-3 px-8 ">
    <div class="flex space-x-4 justify-center">
      <RouterLink
        to="/popular"
        class="text-md hover:text-teal-400 transition duration-300"
      >
        Overview
      </RouterLink>
      <RouterLink
        to="/"
        class="text-md hover:text-teal-400 transition duration-300"
      >
        Media
      </RouterLink>
      <RouterLink
        to="/"
        class="text-md hover:text-teal-400 transition duration-300"
      >
        Fandom
      </RouterLink>

      <RouterLink
        to="/"
        class="text-md hover:text-teal-400 transition duration-300"
      >
        Share
      </RouterLink>
    </div>
  </div>
</template>

<script>
export default {
  name: "SubNavBar",
};
</script>

<style scoped>
/* Add additional styling for the SubNavBar if needed */
</style>
