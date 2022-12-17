<template>
  <div class="search">
    <input type="text" class="search-bar" placeholder="Search" v-model="searchQuery" @keyup.enter="search()" />
    <button class="search-button" @click="search()"><b-icon icon="search"></b-icon></button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      searchQuery: ''
    }
  },
  methods: {
    search: function () {
      this.$root.$emit('searchbarSearch', this.searchQuery)
    }
  }
}
</script>

<style lang="scss" scoped>
.search {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  width: auto;
}
input.search-bar {
  border: none;
  outline: none;
  border-radius: 24px;
  background: #6d4b1f;
  color: var(--white);
  font-family: inherit;
  margin-right: 5px;
  padding-inline: 0.7rem;
  width: 90%;
}
.search-button {
  border-radius: 50%;
  display: flex;
  align-items: center;
  border: none;
  height: 32px;
  width: 35px;
  outline: none;
  background: var(--bg-black);
  color: var(--brilliant-white);
  cursor: pointer;
  transition: 0.2s ease-in-out;
}

@container (max-width: 920px) {
  .search {
    display: flex;
    justify-content: center;
    margin-bottom: 8px;
    width: 100%;
    .search-button { width: 3%; }
    input.search-bar {
      margin-inline: .5rem;
      width: 97%;
    }
  }
}
</style>
