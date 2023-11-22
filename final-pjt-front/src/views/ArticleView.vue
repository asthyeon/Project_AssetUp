<template>
  <div>
    <h1>게시판</h1>
    <hr>
    <RouterLink v-if="userStore.isLogin" :to="{ name: 'article_create' }">
      [CREATE]
    </RouterLink>
    
    <ArticleList v-if="store.articles"/>
    <p v-if="store.articles.length === 0">
      <h3>글이 없습니다.</h3>
    </p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()
const userStore = useUserStore()

onMounted(() => {
  console.log(store.articles);
  store.getArticles()
})

</script>

<style>

</style>
