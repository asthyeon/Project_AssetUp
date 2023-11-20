import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import router from '../router'

export const useArticleStore = defineStore('article', () => {
  const userStore = useUserStore()
  console.log(userStore.token);
  const token = userStore.token
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const name = userStore.name

  // 게시글 전체 불러오기
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 게시글 단일 불러오기
  const articleDetail = ref([])
  const getArticleDetail = function (article_pk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${article_pk}`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((res) => {
      articleDetail.value = res.data
      console.log(articleDetail.value);
    })
    .catch((err) => {
      console.log(err);
    })
  }

  // 게시글 단일 삭제
  const articleDelete = function (article_pk) {
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/articles/${article_pk}`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((res) => {
      router.push({ name: 'articles' })
    })
  }

  return { articles, articleDetail, getArticles, getArticleDetail, articleDelete, API_URL, token, name }
}, { persist: true })
