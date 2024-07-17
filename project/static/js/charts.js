const getOptionChart = async()=>{
  try{
    const response = await fetch('http://127.0.0.1:8000/get-chart/');
  }catch(ex){
    alert(ex);
  }
}

const initChart = async () => {
  const myChart = echarts.init(document.getElementById('chart'));

  myChart.setOption(await getOptionChart())

  myChart.resize()
}

window.addEventListener("Load",async()=>{
  await initChart();
})