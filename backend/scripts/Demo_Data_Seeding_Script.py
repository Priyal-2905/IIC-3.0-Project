"""
Demo Data Seeding Script for Tat-Sahayk Hackathon
Creates realistic demo data for impressive demo presentation
"""
import sys
import os
from datetime import datetime, timedelta
from random import choice, randint, uniform

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models.user import User
from app.models.report import Report
from app.models.alert import Alert
from app.models.red_zone import RedZone
from geoalchemy2 import WKTElement

# Create engine and session
engine = create_engine(str(settings.DATABASE_URL))
SessionLocal = sessionmaker(bind=engine)

def seed_demo_users(db):
    """Create demo citizen users in different cities"""
    demo_users = [
        # Jaipur citizens
        {
            "email": "citizen.jaipur1@demo.com",
            "full_name": "Rajesh Sharma",
            "hashed_password": "$2b$12$dummyhash123456789",  # Won't be used for login
            "role": "citizen",
            "district": "Jaipur",
            "state": "Rajasthan",
            "latitude": 26.9124,
            "longitude": 75.7873,
            "is_active": True
        },
        {
            "email": "citizen.jaipur2@demo.com",
            "full_name": "Priya Meena",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Jaipur",
            "state": "Rajasthan",
            "latitude": 26.8850,
            "longitude": 75.8150,
            "is_active": True
        },
        # Bagru citizens
        {
            "email": "citizen.bagru1@demo.com",
            "full_name": "Vikram Singh",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Bagru",
            "state": "Rajasthan",
            "latitude": 26.8153,
            "longitude": 75.5439,
            "is_active": True
        },
        {
            "email": "citizen.bagru2@demo.com",
            "full_name": "Anita Kumari",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Bagru",
            "state": "Rajasthan",
            "latitude": 26.8200,
            "longitude": 75.5500,
            "is_active": True
        },
        # Mumbai citizens
        {
            "email": "citizen.mumbai1@demo.com",
            "full_name": "Amit Patel",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Mumbai",
            "state": "Maharashtra",
            "latitude": 19.0760,
            "longitude": 72.8777,
            "is_active": True
        },
        {
            "email": "citizen.mumbai2@demo.com",
            "full_name": "Sneha Desai",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Mumbai",
            "state": "Maharashtra",
            "latitude": 19.1136,
            "longitude": 72.8697,
            "is_active": True
        },
        # Chennai citizens
        {
            "email": "citizen.chennai1@demo.com",
            "full_name": "Karthik Kumar",
            "hashed_password": "$2b$12$dummyhash123456789",
            "role": "citizen",
            "district": "Chennai",
            "state": "Tamil Nadu",
            "latitude": 13.0827,
            "longitude": 80.2707,
            "is_active": True
        },
    ]
    
    created_users = []
    for user_data in demo_users:
        existing = db.query(User).filter(User.email == user_data["email"]).first()
        if not existing:
            user = User(**user_data)
            db.add(user)
            created_users.append(user)
    
    db.commit()
    print(f"✅ Created {len(created_users)} demo citizen users")
    return created_users

def seed_demo_reports(db):
    """Create realistic disaster reports"""
    
    # Get demo users and admins
    jaipur_users = db.query(User).filter(User.district == "Jaipur", User.role == "citizen").all()
    mumbai_users = db.query(User).filter(User.district == "Mumbai", User.role == "citizen").all()
    chennai_users = db.query(User).filter(User.district == "Chennai", User.role == "citizen").all()
    bagru_users = db.query(User).filter(User.district == "Bagru", User.role == "citizen").all()
    
    demo_reports = [
        # Jaipur reports
        {
            "user": choice(jaipur_users) if jaipur_users else None,
            "hazard_type": "Flood",
            "description": "Heavy waterlogging near Amber Fort area. Road completely submerged, vehicles stranded.",
            "severity": "high",
            "lat": 26.9855,
            "lon": 75.8513,
            "district": "Jaipur",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.89,
            "created_hours_ago": 2
        },
        {
            "user": choice(jaipur_users) if jaipur_users else None,
            "hazard_type": "Storm",
            "description": "Strong winds causing damage to temporary structures in Mansarovar area. Trees uprooted.",
            "severity": "medium",
            "lat": 26.8593,
            "lon": 75.7766,
            "district": "Jaipur",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.92,
            "created_hours_ago": 5
        },
        {
            "user": choice(jaipur_users) if jaipur_users else None,
            "hazard_type": "Flood",
            "description": "Water level rising in low-lying areas near Jal Mahal. Nearby colonies at risk.",
            "severity": "high",
            "lat": 26.9523,
            "lon": 75.8461,
            "district": "Jaipur",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.86,
            "created_hours_ago": 1
        },
        {
            "user": choice(jaipur_users) if jaipur_users else None,
            "hazard_type": "Flood",
            "description": "Sanganer area facing severe waterlogging. Market area flooded.",
            "severity": "medium",
            "lat": 26.8167,
            "lon": 75.8125,
            "district": "Jaipur",
            "status": "pending",
            "is_verified": False,
            "ai_authenticity_score": 0.75,
            "created_hours_ago": 0.5
        },
        
        # Bagru reports
        {
            "user": choice(bagru_users) if bagru_users else None,
            "hazard_type": "Flood",
            "description": "Flash flood in Bagru village. Water entered homes near Bagru Dam area. Urgent help needed.",
            "severity": "critical",
            "lat": 26.8153,
            "lon": 75.5439,
            "district": "Bagru",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.93,
            "created_hours_ago": 1.5
        },
        {
            "user": choice(bagru_users) if bagru_users else None,
            "hazard_type": "Storm",
            "description": "Heavy winds damaging kaccha houses in rural Bagru area. Several roofs blown off.",
            "severity": "high",
            "lat": 26.8200,
            "lon": 75.5500,
            "district": "Bagru",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.88,
            "created_hours_ago": 3
        },
        
        # Mumbai reports
        {
            "user": choice(mumbai_users) if mumbai_users else None,
            "hazard_type": "Cyclone",
            "description": "Cyclonic winds hitting coastal areas. Marine Drive experiencing high waves and flooding.",
            "severity": "critical",
            "lat": 18.9432,
            "lon": 72.8236,
            "district": "Mumbai",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.94,
            "created_hours_ago": 3
        },
        {
            "user": choice(mumbai_users) if mumbai_users else None,
            "hazard_type": "Flood",
            "description": "Heavy rainfall causing waterlogging in Andheri subway. Traffic completely halted.",
            "severity": "high",
            "lat": 19.1136,
            "lon": 72.8697,
            "district": "Mumbai",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.91,
            "created_hours_ago": 4
        },
        {
            "user": choice(mumbai_users) if mumbai_users else None,
            "hazard_type": "Cyclone",
            "description": "Strong winds in Worli area. Hoardings and temporary structures damaged.",
            "severity": "high",
            "lat": 19.0177,
            "lon": 72.8150,
            "district": "Mumbai",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.88,
            "created_hours_ago": 2
        },
        {
            "user": choice(mumbai_users) if mumbai_users else None,
            "hazard_type": "Flood",
            "description": "Bandra reclamation area facing severe flooding. Residents evacuating.",
            "severity": "critical",
            "lat": 19.0596,
            "lon": 72.8295,
            "district": "Mumbai",
            "status": "pending",
            "is_verified": False,
            "ai_authenticity_score": 0.82,
            "created_hours_ago": 1
        },
        
        # Chennai reports
        {
            "user": choice(chennai_users) if chennai_users else None,
            "hazard_type": "Flood",
            "description": "Heavy flooding in Velachery area. Ground floor apartments inundated.",
            "severity": "high",
            "lat": 12.9759,
            "lon": 80.2207,
            "district": "Chennai",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.90,
            "created_hours_ago": 6
        },
        {
            "user": choice(chennai_users) if chennai_users else None,
            "hazard_type": "Storm",
            "description": "Strong coastal winds affecting Besant Nagar beach area. High tide causing erosion.",
            "severity": "medium",
            "lat": 13.0002,
            "lon": 80.2668,
            "district": "Chennai",
            "status": "verified",
            "is_verified": True,
            "ai_authenticity_score": 0.87,
            "created_hours_ago": 3
        },
    ]
    
    created_reports = []
    for report_data in demo_reports:
        if report_data["user"]:
            report = Report(
                user_id=report_data["user"].id,
                hazard_type=report_data["hazard_type"],
                description=report_data["description"],
                severity=report_data["severity"],
                location=WKTElement(f'POINT({report_data["lon"]} {report_data["lat"]})', srid=4326),
                district=report_data["district"],
                status=report_data["status"],
                is_verified=report_data["is_verified"],
                ai_authenticity_score=report_data["ai_authenticity_score"],
                ai_analysis_summary="AI-verified: Authentic disaster report based on image analysis and contextual verification.",
                confirmation_count=randint(3, 15),
                created_at=datetime.utcnow() - timedelta(hours=report_data["created_hours_ago"])
            )
            db.add(report)
            created_reports.append(report)
    
    db.commit()
    print(f"✅ Created {len(created_reports)} demo reports")

def seed_demo_alerts(db):
    """Create demo alerts and circulars"""
    
    # Get admin users
    jaipur_admin = db.query(User).filter(User.email == "admin.jaipur@tatsahayk.gov.in").first()
    mumbai_admin = db.query(User).filter(User.email == "admin.mumbai@tatsahayk.gov.in").first()
    chennai_admin = db.query(User).filter(User.email == "admin.chennai@tatsahayk.gov.in").first()
    bagru_admin = db.query(User).filter(User.email == "admin.bagru@tatsahayk.gov.in").first()
    national_admin = db.query(User).filter(User.email == "admin.national@tatsahayk.gov.in").first()
    
    demo_alerts = [
        # Jaipur emergency alerts
        {
            "admin": jaipur_admin,
            "title": "Flash Flood Warning - Jaipur District",
            "message": "Heavy rainfall expected in next 6 hours. Low-lying areas near Jal Mahal and Amber Fort may experience flooding. Residents advised to move to higher ground. Emergency helpline: 1077",
            "hazard_type": "flood",
            "severity": "high",
            "district": "Jaipur",
            "state": "Rajasthan",
            "hours_ago": 2
        },
        {
            "admin": jaipur_admin,
            "title": "Storm Alert - Sanganer Area",
            "message": "Strong winds (60-70 km/h) expected this evening. Secure loose objects and avoid venturing out. Market areas advised to close early.",
            "hazard_type": "storm",
            "severity": "medium",
            "district": "Jaipur",
            "state": "Rajasthan",
            "hours_ago": 4
        },
        
        # Bagru emergency alerts
        {
            "admin": bagru_admin,
            "title": "Critical Flash Flood Warning - Bagru Dam Area",
            "message": "Flash flood alert issued for Bagru village area. Water level rising rapidly near dam. Immediate evacuation advised for low-lying areas. Emergency helpline: 1077",
            "hazard_type": "flood",
            "severity": "critical",
            "district": "Bagru",
            "state": "Rajasthan",
            "hours_ago": 1
        },
        {
            "admin": bagru_admin,
            "title": "Relief Camp Set Up - Bagru",
            "message": "Emergency relief camp operational at Bagru Government School. Free food, medical aid, and shelter available. All residents advised to move to safety.",
            "hazard_type": "info",
            "severity": "medium",
            "district": "Bagru",
            "state": "Rajasthan",
            "hours_ago": 2
        },
        
        # Mumbai emergency alerts
        {
            "admin": mumbai_admin,
            "title": "Cyclone Warning - Mumbai Coastal Areas",
            "message": "Cyclonic system approaching Mumbai coast. Red alert issued. Marine Drive, Worli, and Bandra areas at high risk. Avoid coastal areas. Emergency services on standby.",
            "hazard_type": "cyclone",
            "severity": "critical",
            "district": "Mumbai",
            "state": "Maharashtra",
            "hours_ago": 1
        },
        {
            "admin": mumbai_admin,
            "title": "Heavy Rainfall Alert",
            "message": "Extremely heavy rainfall predicted for next 12 hours. Waterlogging expected in low-lying areas. Stay indoors if possible. NDRF teams deployed.",
            "hazard_type": "flood",
            "severity": "high",
            "district": "Mumbai",
            "state": "Maharashtra",
            "hours_ago": 3
        },
        
        # Chennai alerts
        {
            "admin": chennai_admin,
            "title": "Flood Advisory - Velachery Region",
            "message": "Water levels rising in Velachery lake. Nearby areas may experience flooding. Residents of low-lying areas advised to evacuate to relief centers.",
            "hazard_type": "flood",
            "severity": "high",
            "district": "Chennai",
            "state": "Tamil Nadu",
            "hours_ago": 5
        },
        
        # Circulars (info messages)
        {
            "admin": jaipur_admin,
            "title": "Relief Camp Locations - Jaipur",
            "message": "Relief camps set up at: 1) Jawahar Circle Garden, 2) SMS Stadium, 3) Central Park. Free food, medical aid, and shelter available 24/7.",
            "hazard_type": "info",
            "severity": "low",
            "district": "Jaipur",
            "state": "Rajasthan",
            "hours_ago": 6
        },
        {
            "admin": mumbai_admin,
            "title": "Essential Services Update",
            "message": "All government hospitals operating 24/7. Additional ambulances deployed. Drinking water supply maintained. Power restoration teams active.",
            "hazard_type": "info",
            "severity": "low",
            "district": "Mumbai",
            "state": "Maharashtra",
            "hours_ago": 4
        },
        {
            "admin": national_admin,
            "title": "National Weather Advisory",
            "message": "IMD predicts heavy monsoon activity over Western and Central India for next 48 hours. All states advised to activate disaster management protocols.",
            "hazard_type": "info",
            "severity": "medium",
            "district": None,  # National alert
            "state": None,
            "hours_ago": 8
        },
    ]
    
    created_alerts = []
    for alert_data in demo_alerts:
        if alert_data["admin"]:
            alert = Alert(
                admin_id=alert_data["admin"].id,
                title=alert_data["title"],
                message=alert_data["message"],
                hazard_type=alert_data["hazard_type"],
                severity=alert_data["severity"],
                district=alert_data["district"],
                state=alert_data["state"],
                is_active=True,
                created_at=datetime.utcnow() - timedelta(hours=alert_data["hours_ago"]),
                expires_at=datetime.utcnow() + timedelta(hours=24)
            )
            db.add(alert)
            created_alerts.append(alert)
    
    db.commit()
    print(f"✅ Created {len(created_alerts)} demo alerts and circulars")

def seed_demo_red_zones(db):
    """Create demo red zones"""
    
    demo_red_zones = [
        {
            "name": "Amber Fort Flood Zone",
            "district": "Jaipur",
            "state": "Rajasthan",
            "center_lat": 26.9855,
            "center_lon": 75.8513,
            "radius_km": 2.5,
            "intensity": "high",
            "hazard_types": ["flood", "waterlogging"],
            "description": "Area experiencing severe waterlogging due to continuous rainfall. Roads submerged."
        },
        {
            "name": "Bagru Dam Flood Zone",
            "district": "Bagru",
            "state": "Rajasthan",
            "center_lat": 26.8153,
            "center_lon": 75.5439,
            "radius_km": 3.0,
            "intensity": "critical",
            "hazard_types": ["flood", "dam_overflow"],
            "description": "Critical flood situation near Bagru Dam. Water level rising rapidly. Immediate evacuation recommended."
        },
        {
            "name": "Marine Drive Cyclone Zone",
            "district": "Mumbai",
            "state": "Maharashtra",
            "center_lat": 18.9432,
            "center_lon": 72.8236,
            "radius_km": 3.0,
            "intensity": "critical",
            "hazard_types": ["cyclone", "high_tide"],
            "description": "Coastal area under cyclone threat. High waves and strong winds reported."
        },
        {
            "name": "Velachery Flood Area",
            "district": "Chennai",
            "state": "Tamil Nadu",
            "center_lat": 12.9759,
            "center_lon": 80.2207,
            "radius_km": 2.0,
            "intensity": "high",
            "hazard_types": ["flood"],
            "description": "Low-lying residential area with severe flooding. Ground floors inundated."
        },
    ]
    
    created_zones = []
    for zone_data in demo_red_zones:
        # Check if zone already exists
        existing = db.query(RedZone).filter(RedZone.name == zone_data["name"]).first()
        if not existing:
            red_zone = RedZone(
                name=zone_data["name"],
                district=zone_data["district"],
                state=zone_data["state"],
                center_point=WKTElement(f'POINT({zone_data["center_lon"]} {zone_data["center_lat"]})', srid=4326),
                radius_km=zone_data["radius_km"],
                intensity=zone_data["intensity"],
                hazard_types=zone_data["hazard_types"],
                description=zone_data["description"],
                is_active=True
            )
            db.add(red_zone)
            created_zones.append(red_zone)
    
    db.commit()
    print(f"✅ Created {len(created_zones)} demo red zones")

def seed_demo_activity(db):
    """Create demo user activity records"""
    
    # Get all users
    all_users = db.query(User).filter(User.role == "citizen").all()
    
    if not all_users:
        print("⚠️  No users found, skipping activity seeding")
        return
    
    # Create activity records for last 3 hours
    activity_types = ['app_open', 'login', 'report_submit', 'safety_check']
    
    activities_created = 0
    for _ in range(30):  # Create 30 random activities
        user = choice(all_users)
        activity_type = choice(activity_types)
        hours_ago = uniform(0, 3)  # Random time in last 3 hours
        
        # Use raw SQL to insert activity
        query = text("""
            INSERT INTO user_activities (user_id, activity_type, district, state, timestamp)
            VALUES (:user_id, :activity_type, :district, :state, :timestamp)
        """)
        
        db.execute(query, {
            "user_id": user.id,
            "activity_type": activity_type,
            "district": user.district,
            "state": user.state,
            "timestamp": datetime.utcnow() - timedelta(hours=hours_ago)
        })
        activities_created += 1
    
    db.commit()
    print(f"✅ Created {activities_created} demo activity records")

def main():
    print("🌟 Starting Demo Data Seeding for Tat-Sahayk Hackathon Demo\n")
    
    db = SessionLocal()
    
    try:
        # Check if activity table exists
        try:
            result = db.execute(text("SELECT COUNT(*) FROM user_activities")).scalar()
            print(f"ℹ️  Activity table exists with {result} records\n")
        except Exception:
            print("⚠️  Activity table doesn't exist! Run create_activity_table.py first\n")
        
        # Seed data
        print("📊 Seeding demo users...")
        seed_demo_users(db)
        
        print("\n📍 Seeding demo reports...")
        seed_demo_reports(db)
        
        print("\n🚨 Seeding demo alerts...")
        seed_demo_alerts(db)
        
        print("\n⚠️  Seeding demo red zones...")
        seed_demo_red_zones(db)
        
        print("\n📈 Seeding demo activity records...")
        seed_demo_activity(db)
        
        print("\n" + "="*60)
        print("✅ DEMO DATA SEEDING COMPLETE!")
        print("="*60)
        print("\n🎯 Your database now has:")
        print("   • ~12 realistic disaster reports (Jaipur, Bagru, Mumbai, Chennai)")
        print("   • ~10 government alerts and circulars")
        print("   • ~4 red zones")
        print("   • ~7 demo citizen users")
        print("   • ~30 activity records (shows 'active users')")
        print("\n🎬 Ready for an impressive hackathon demo!")
        print("\n💡 Demo Credentials:")
        print("   Jaipur Admin: admin.jaipur@tatsahayk.gov.in / JAIPUR_ADMIN_123")
        print("   Bagru Admin:  admin.bagru@tatsahayk.gov.in / BAGRU_ADMIN_123")
        print("   Mumbai Admin: admin.mumbai@tatsahayk.gov.in / MUMBAI_ADMIN_123")
        print("   Chennai Admin: admin.chennai@tatsahayk.gov.in / CHENNAI_ADMIN_123")
        
    except Exception as e:
        print(f"\n❌ Error seeding data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()
