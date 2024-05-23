<template>
  <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#">Federated Learing</a>
  </header>
  <div class="container-fluid">
    <div class="row">
      <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
        <div class="position-sticky pt-3 sidebar-sticky">
          <ul class="nav flex-column">
            <li class="nav-item">
              <a href="#" class="nav-link" @click="changePage('page1')">项目训练</a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" @click="changePage('page2')">项目预测</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="users" class="align-text-bottom"></span>
                成员管理
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="bar-chart-2" class="align-text-bottom"></span>
                项目设置
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="layers" class="align-text-bottom"></span>
                个人中心
              </a>
            </li>
          </ul>

          <h6
            class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted text-uppercase">
            <span>项目管理</span>
            <a class="link-secondary" href="#" aria-label="Add a new report">
              <span data-feather="plus-circle" class="align-text-bottom"></span>
            </a>
          </h6>
          <ul class="nav flex-column mb-2">
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="file-text" class="align-text-bottom"></span>
                历史记录
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="file-text" class="align-text-bottom"></span>
                操作指南
              </a>
            </li>
          </ul>
        </div>
      </nav>

      <main v-show="currentPage === 'page1'" class="home-content col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <div
          class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
          <h2 class="h2">{{ projectName }}</h2>
        </div>
        <div class="home-content-body">
          <div class="home-content-body-startTrain">
            <div class="input-group home-content-body-startTrain-input">
              <input type="file" class="form-control" @change="validateFile" ref="fileInput">
              <button type="button" class="btn btn-primary submit" @click="submitFile">上传文件</button>
            </div>
          </div>
          <div class="home-content-body-select">
            <div class="input-group select-model">
              <select class="form-select" aria-label="Default select example">
                <option class="option-disabled" disabled value="">请选择模型结构</option>
                <option>逻辑斯特回归</option>
                <option>朴素贝叶斯模型</option>
                <option>决策树</option>
                <option>SVD模型</option>
                <option>K-means聚类</option>
                <option>随机森林模型</option>
              </select>
            </div>
            <div class="input-group select-epoch">
              <select class="form-select" aria-label="Default select example">
                <option class="option-disabled" disabled value="">请选择训练轮次</option>
                <option>64</option>
                <option>128</option>
                <option>512</option>
              </select>
            </div>
            <div class="input-group select-lr">
              <select class="form-select" aria-label="Default select example">
                <option class="option-disabled" disabled value="">请选择学习率</option>
                <option>0.1</option>
                <option>0.01</option>
                <option>0.001</option>
              </select>
            </div>
          </div>
          <button type="button" class="btn btn-primary submit" @click="startTrain"
            style="margin:5px 0 0 15px">开始训练</button>
        </div>
        <!-- 加载动画 -->
        <div v-if="isLoading" class="loading-overlay">
          <div class="loading-spinner"></div>
        </div>
        <!-- 显示图片 -->
        <div>
          <div v-for="(imgUrl, index) in images" :key="index">
            <img :src="imgUrl" alt="Image" style="height:400px; width:1000px">
          </div>
        </div>
      </main>
      <main v-show="currentPage === 'page2'" class="home-content col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <div
          class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
          <h2 class="h2">{{ projectName }}</h2>
        </div>
        <div class="home-content-body">
          <div class="home-content-body-startPredict">
            <div class="input-group home-content-body-startPredict-input">
              <input type="file" class="form-control" @change="validateFile" ref="fileInput">
              <button type="button" class="btn btn-primary submit" @click="submitFile">上传文件</button>
            </div>
          </div>
          <div class="home-content-body-select">
            <div class="input-group select-model">
              <select class="form-select" aria-label="Default select example">
                <option class="option-disabled" disabled value="">请选择模型结构</option>
                <option>4agfdv5y</option>
                <option>2gdf6743</option>
                <option>8vsdg245</option>
              </select>
            </div>
          </div>
          <button type="button" class="btn btn-primary submit" @click="startPredict"
            style="margin:5px 0 0 15px">开始预测</button>
        </div>
        <!-- 加载动画 -->
        <div v-if="isLoading" class="loading-overlay">
          <div class="loading-spinner"></div>
        </div>
        <div class="home-content-body-iframe">
          <iframe :src="iframeSrc" width="100%" @load="adjustIframeHeight" ref="iframeRef"></iframe>
        </div>
      </main>
    </div>
  </div>

</template>

<style scoped src='../css/dashboard.css'></style>
<script setup>
// eslint-disable-next-line
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import JSZip from 'jszip'

// 上方栏页面切换
// eslint-disable-next-line
let currentPage = ref('page1') // 默认显示第一个页面
// eslint-disable-next-line
const changePage = (page) => {
  currentPage.value = page
}

const route = useRoute()
// eslint-disable-next-line
const projectName = route.params.name

const fileInput = ref(null)
const allowedExtensions = ['csv', 'xlsx', 'xsl', 'docx']

const validateFile = () => {
  const selectedFile = fileInput.value.files[0]
  if (selectedFile) {
    const fileName = selectedFile.name
    const fileExtension = fileName.split('.').pop()
    if (!allowedExtensions.includes(fileExtension)) {
      alert('文件格式不正确')
      return false
    }
    return true
  }
  return false
}

// eslint-disable-next-line
const submitFile = () => {
  if (validateFile()) {
    const formData = new FormData()
    const selectedFile = fileInput.value.files[0]
    formData.append('file', selectedFile)
    formData.append('project_name', projectName)
    console.log(formData)

    axios.post('http://10.29.75.164:8000/upload_predict_data/', formData)
      .then(response => {
        console.log(response.data)
        alert('上传成功')
        // 处理响应数据
      })
      .catch(error => {
        console.error(error)
        alert('上传失败')
        // 处理错误
      })
  }
}

const isLoading = ref(false) // 加载状态
const iframeSrc = ref('')
// eslint-disable-next-line
const startPredict = async () => {
  isLoading.value = true // 开始加载
  try {
    const response = await axios.post('http://10.29.75.164:8000/start_predict/')
    iframeSrc.value = window.URL.createObjectURL(new Blob([response.data], { type: 'text/html' }))
  } catch (error) {
    console.error(error)
    alert('预测失败')
  } finally {
    isLoading.value = false // 结束加载
  }
}

const iframeRef = ref(null)
// eslint-disable-next-line
const adjustIframeHeight = () => {
  const iframe = iframeRef.value
  if (iframe && iframe.contentWindow && iframe.contentWindow.document) {
    // 获取iframe的内容高度
    const documentHeight = iframe.contentWindow.document.documentElement.scrollHeight
    // 设置iframe的高度
    iframe.style.height = `${documentHeight}px`
  }
}

const images = ref([]) // 使用 ref 创建响应式数组
// eslint-disable-next-line
const startTrain = async () => {
  isLoading.value = true // 开始加载
  try {
    const response = await axios.get('http://10.29.75.164:8000/start_training/', { responseType: 'blob' })
    alert('训练成功')
    const zip = await JSZip.loadAsync(response.data)
    for (const filename of Object.keys(zip.files)) {
      const fileData = await zip.files[filename].async('blob')
      const imgUrl = URL.createObjectURL(fileData)
      images.value.push(imgUrl) // 直接添加图片 URL 到 images 数组
    }
  } catch (error) {
    console.error(error)
    alert('训练失败')
  } finally {
    isLoading.value = false // 结束加载
  }
}
</script>
