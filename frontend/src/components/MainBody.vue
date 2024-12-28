<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "MainBody",
  setup() {
    const movieData = ref(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
        );
        movieData.value = response.data;
        console.log(movieData.value);
      } catch (error) {
        console.error("Error fetching movie data:", error);
      }
    });

    return { movieData };
  },
};
</script>

<template>
  <div class="">
    <div class="flex flex-col items-center p-6 bg-gradient-to-r from-[#022a61] via-[#242832] to-[#061f4b] text-white font-sans sm:flex-row sm:gap-6">
      <!-- Left Section: Movie Poster -->
      <div class="flex flex-col items-center mb-6 sm:mb-0 sm:items-start">
        <img
          :src="movieData?.Poster || 'https://via.placeholder.com/300x450'"
          alt="Movie Poster"
          class="w-72 h-auto rounded-lg mb-4 transition-transform duration-300 transform hover:scale-110"
        />
        <div class="text-center">
          <p>Now Streaming</p>
          <button class="bg-[#01b4e4] text-white py-2 px-4 rounded mt-2 hover:bg-[#008dc8] transition-colors duration-300">
            Watch Now
          </button>
        </div>
      </div>

      <!-- Right Section: Movie Details -->
      <div class="flex-1 text-center sm:text-left">
        <h1 class="text-3xl font-bold mb-4">
          {{ movieData?.Title || "Loading..." }}
          <span class="text-xl text-[#90cea1]">({{ movieData?.Year || "N/A" }})</span>
        </h1>
        <p class="text-lg mb-6">
          {{ movieData?.Rated || "N/A" }} | {{ movieData?.Released || "TBD" }} |
          {{ movieData?.Genre || "N/A" }} | {{ movieData?.Runtime || "N/A" }}
        </p>
        <div class="flex items-center justify-center gap-4 mb-6 sm:justify-start">
          <span class="text-2xl font-bold text-[#90cea1]">76%</span>
          <p>User Score</p>
        </div>
        <div class="justify-start fixed bottom-0 left-0 w-full bg-gray-900 p-4 flex flex-row  sm:relative sm:bg-transparent sm:p-0 sm:flex sm:space-x-4">
  <button class="bg-[#0b0b0b] text-white py-2 px-4 rounded w-full sm:w-auto hover:bg-[#008dc8] transition-colors duration-300">
    ❤ Like
  </button>
  <button class="bg-[#0b0b0b] text-white py-2 px-4 rounded w-full sm:w-auto hover:bg-[#008dc8] transition-colors duration-300">
    ➕ Watchlist
  </button>
  <button class="bg-[#0b0b0b] text-white py-2 px-4 rounded w-full sm:w-auto hover:bg-[#008dc8] transition-colors duration-300">
    ▶ Trailer
  </button>
</div>
        <div class="mb-6">
          <h2 class="text-2xl font-semibold mb-2">Overview</h2>
          <p>{{ movieData?.Plot || "No overview available." }}</p>
        </div>
        <div>
          <h3 class="text-xl font-semibold mb-2">Contributors</h3>
          <ul class="list-none p-0">
            <li class="mb-2">Director - {{ movieData?.Director }}</li>
            <li class="mb-2">Writers - {{ movieData?.Writer }}</li>
            <li class="mb-2">Actors - {{ movieData?.Actors }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>