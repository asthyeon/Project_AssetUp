<template>
  <div>
    <h5>{{ board_article.id }}</h5>
    <p>{{ board_article.user_name }}</p>
    <p>{{ board_article.title }}</p>
    <p>{{ board_article.content }}</p>
    <RouterLink :to="{ name: 'board_detail', params: { id: board_article.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  board_article: Object
})
</script>
