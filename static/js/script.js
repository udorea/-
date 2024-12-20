document.getElementById('calculator-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // 사용자 입력값 가져오기
    const mass = document.getElementById('mass').value;
    const distance = document.getElementById('distance').value;

    // 서버에 데이터 전송
    fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mass: mass, distance: distance })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('오류: ' + data.error);
        } else {
            // 결과 표시
            document.getElementById('velocity').textContent = data.velocity.toFixed(2) + " m/s";  // 궤도 속도
            document.getElementById('period').textContent = 
                `${data.period_seconds.toFixed(2)} 초 (${data.period_days.toFixed(2)} 일)`;  // 공전 주기
            document.getElementById('earth-mass').textContent = 
                `지구의 질량: ${data.earth_mass_kg.toFixed(2)} kg`;  // 지구 질량
            document.getElementById('sun-earth-distance').textContent = 
                `태양과 지구의 평균 거리: ${(data.sun_earth_distance_m / 1000).toFixed(2)} km`;  // 태양과 지구의 거리 (km로 변환)
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
