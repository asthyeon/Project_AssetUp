import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useHomeStore = defineStore('home', () => {
  const dps = ref(null)
  const sps = ref(null)
  const allps = ref(null)
  const topDps = ref([])
  const topSps = ref([])
  const topAllps = ref([])

  // 예금
  const getDps = () => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/finances/top-dps/'
    })
    .then((res) => {
      dps.value = res.data.map(item => item[1])
      console.log(dps.value);
      getTopDps()
    })
  }

  const getTopDps = () => {
    topDps.value = []
    for (let i = 0; i < 3; i++) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/finances/get-deposit-product-detail/${dps.value[i]}/`
      })
      .then((res) => {
        topDps.value.push(res.data)
        console.log(res.data[0].product);
      })
      .catch((err) => {
        console.log(err);
      })
    }
  }

  // 적금
  const getSps = () => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/finances/top-sps/'
    })
    .then((res) => {
      sps.value = res.data.map(item => item[1])
      console.log(sps.value);
      getTopSps()
    })
  }
  const getTopSps = () => {
    topSps.value = []
    for (let i = 0; i < 3; i++) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/finances/get-saving-product-detail/${sps.value[i]}/`
      })
      .then((res) => {
        topSps.value.push(res.data)
        console.log(topSps.value);
      })
      .catch((err) => {
        console.log(err);
      })
    }
  }

  // // 연금
  // const getAps = () => {
  //   axios({
  //     method: 'get',
  //     url: 'http://127.0.0.1:8000/finances/top-aps/'
  //   })
  //   .then((res) => {
  //     aps.value = res.data.map(item => item[1])
  //     console.log(aps.value);
  //     getTopAps()
  //   })
  // }
  // const getTopAps = () => {
  //   topAps.value = []
  //   for (let i = 0; i < 3; i++) {
  //     axios({
  //       method: 'get',
  //       url: `http://127.0.0.1:8000/finances/get-annuity-saving-product-detail/${aps.value[i]}/`
  //     })
  //     .then((res) => {
  //       topAps.value.push(res.data)
  //       console.log(topAps.value);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     })
  //   }
  // }
  const getAllps = () => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/finances/best-three/'
    })
    .then((res) => {
      allps.value = res.data.map(item => item[1])
      console.log(allps.value);
      getTopAllps()
    })
  }
  const getTopAllps = () => {
    topAllps.value = []
    for (let i = 0; i < 3; i++) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/finances/get-saving-product-detail/${sps.value[i]}/`
      })
      .then((res) => {
        topAllps.value.push(res.data)
        console.log(topAllps.value);
      })
      .catch((err) => {
        console.log(err);
      })
    }
  }
  
  // 모든 top3 가져오기
  const getAll = () => {
    getDps()
    getSps()
    getAllps()
    // getAps()
  }

  

  return { getAll, topDps, topSps, topAllps }
}, { persist: true })
