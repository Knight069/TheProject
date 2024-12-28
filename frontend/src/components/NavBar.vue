<template>
  <header class="bg-gray-900 text-white py-4 sticky top-0 z-50 shadow-lg">
    <div class="wrapper mx-auto flex justify-between items-center px-8">
      <!-- Left Section -->
      <div class="flex items-center space-x-6">
        <button
          @click="isMenuOpen = !isMenuOpen"
          class="md:hidden focus:outline-none"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16m-7 6h7"
            ></path>
          </svg>
        </button>
        <button
          to="/"
          class="text-2xl font-bold hover:text-teal-400 transition duration-300"
        >
          TMDB
        </button>
      </div>

      <!-- Center Section (for larger screens) -->
      <nav class="hidden md:flex items-center space-x-6">
        <div class="relative group">
          <button
            to="/movies"
            class="text-lg hover:text-teal-400 transition duration-300"
          >
            Movies
          </button>
          <div
            class="absolute hidden group-hover:block bg-gray-800 text-white py-2 rounded shadow-lg"
          >
            <button
              to="/popular-movies"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              Popular
            </button>
            <button
              to="/top-rated-movies"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              Top Rated
            </button>
            <button
              to="/upcoming-movies"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              Upcoming
            </button>
          </div>
        </div>

        <div class="relative group">
          <button
            to="/tv-shows"
            class="text-lg hover:text-teal-400 transition duration-300"
          >
            TV Shows
          </button>
          <div
            class="absolute hidden group-hover:block bg-gray-800 text-white py-2 rounded shadow-lg"
          >
            <button
              to="/popular-tv-shows"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              Popular
            </button>
            <button
              to="/top-rated-tv-shows"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              Top Rated
            </button>
            <button
              to="/on-the-air"
              class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
            >
              On The Air
            </button>
          </div>
        </div>

        <button
          to="/people"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          People
        </button>
        <button
          to="/more"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          More
        </button>
      </nav>

      <!-- Right Section -->
      <nav class="hidden md:flex items-center space-x-6">
        <button
          to="/add-content"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          +
        </button>
        <button
          to="/language"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          EN
        </button>
        <button
          to="/login"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          Login
        </button>
        <button
          to="/join"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          Join TMDB
        </button>
        <button
          to="/search"
          @click="toggleDropdown"
          class="text-lg hover:text-teal-400 transition duration-300"
        >
          Search Icon
        </button>
      </nav>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isMenuOpen" class="bg-gray-800 md:hidden">
      <nav class="flex flex-col space-y-2 py-4 px-8">
        <button
          to="/movies"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          Movies
        </button>
        <button
          to="/popular-movies"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          Popular
        </button>
        <button
          to="/top-rated-movies"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          Top Rated
        </button>
        <button
          to="/upcoming-movies"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          Upcoming
        </button>
        <button
          to="/tv-shows"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          TV Shows
        </button>
        <button
          to="/popular-tv-shows"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          Popular
        </button>
        <button
          to="/top-rated-tv-shows"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          Top Rated
        </button>
        <button
          to="/on-the-air"
          class="block px-4 py-2 hover:bg-gray-700 transition duration-300"
          @click="isMenuOpen = false"
        >
          On The Air
        </button>
        <button
          to="/people"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          People
        </button>
        <button
          to="/more"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          More
        </button>
        <button
          to="/add-content"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          +
        </button>
        <button
          to="/language"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          EN
        </button>
        <button
          to="/login"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          Login
        </button>
        <button
          to="/join"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          Join TMDB
        </button>
        <button
          to="/search"
          class="text-lg hover:text-teal-400 transition duration-300"
          @click="isMenuOpen = false"
        >
          Search Icon
        </button>
      </nav>
    </div>

    <!-- Search Dropdown -->
    <div v-if="isDropdownOpen" class="absolute mt-2 bg-white shadow-lg rounded-lg p-4 w-full max-w-md">
      <form @submit.prevent="performSearch">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="w-full p-2 border border-gray-300 rounded mb-2"
        />
        <button
          type="submit"
          class="bg-[#01b4e4] text-white py-2 px-4 rounded hover:bg-[#008dc8] transition-colors duration-300"
        >
          Search
        </button>
      </form>
    </div>
  </header>
</template>

<script>
import { ref } from "vue";
import axios from 'axios';

export default {
  name: "NavBar",
  data() {
    return {
      isMenuOpen: false,
      isDropdownOpen: false,
      searchQuery: ""
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    async performSearch() {
      try {
        const response = await axios.get(`https://api.example.com/search?q=${this.searchQuery}`);
        console.log("Search results:", response.data);
        // Handle the search results as needed
      } catch (error) {
        console.error("Error performing search:", error);
      }
      this.isDropdownOpen = false; // Close the dropdown after search
    }
  }
};
</script>

<style scoped>
/* Add hover effect for dropdown */
.group:hover > div {
  display: block;
}
</style>