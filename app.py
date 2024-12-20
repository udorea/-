from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)



# 지구 질량 (kg), e 표기법 사용
EARTH_MASS_KG = 5.972e24  # 지구 질량 (kg)
SUN_MASS_KG = 1.989e30  # 태양 질량 (kg)

# 태양과 지구 사이의 평균 거리 (km) -> m로 변환
SUN_EARTH_DISTANCE_KM = 1.5e11  # 약 1억 4천9백60만 km
SUN_EARTH_DISTANCE_M = SUN_EARTH_DISTANCE_KM * 1000  # m로 변환

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 계산 API
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # 사용자가 보낸 데이터 가져오기
        data = request.json
        mass = float(data['mass'])  # 행성의 질량 (kg)
        distance = float(data['distance'])  # 중심에서의 거리 (m)

        # 중력 상수
        G = 6.67430e-11  

        # 궤도 속도 계산: v = sqrt(G * M / r)
        velocity = math.sqrt(G * mass / distance)

        # 공전 주기 계산: T = 2π * sqrt(r^3 / (G * M))
        period_seconds = 2 * math.pi * math.sqrt(distance**3 / (G * SUN_MASS_KG))

        # 초를 일 단위로 변환
        period_days = period_seconds / 86400

        # 결과 반환
        return jsonify({
            'velocity': velocity, 
            'period_seconds': period_seconds, 
            'period_days': period_days,
            'earth_mass_kg': EARTH_MASS_KG,  # 지구 질량
            'sun_earth_distance_m': SUN_EARTH_DISTANCE_M  # 태양과 지구 사이의 거리 (m)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
