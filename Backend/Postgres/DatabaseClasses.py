from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LinkedInExperience(Base):
    __tablename__ = 'tbl_linkedinexperience'
    experience_id = Column(Integer, primary_key=True)
    public_identifier = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    company = Column(String)
    company_linkedin_profile_url = Column(String)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    logo_url = Column(String)
    last_updated = Column(Date)

    def __repr__(self):
        return f"LinkedInExperience(experience_id={self.experience_id}, public_identifier={self.public_identifier}, start_date={self.start_date}, end_date={self.end_date}, company={self.company}, company_linkedin_profile_url={self.company_linkedin_profile_url}, title={self.title}, description={self.description}, location={self.location}, logo_url={self.logo_url}, last_updated={self.last_updated})"


class LinkedInProfile(Base):
    __tablename__ = 'tbl_linkedinprofile'
    public_identifier = Column(String, primary_key=True)
    profile_pic_url = Column(String)
    background_cover_image_url = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)
    follower_count = Column(String)
    occupation = Column(String)
    headline = Column(String)
    summary = Column(String)
    country = Column(String)
    country_full_name = Column(String)
    city = Column(String)
    state = Column(String)

    def __repr__(self):
        return f"LinkedInProfile(public_identifier={self.public_identifier}, profile_pic_url={self.profile_pic_url}, background_cover_image_url={self.background_cover_image_url}, first_name={self.first_name}, last_name={self.last_name}, full_name={self.full_name}, follower_count={self.follower_count}, occupation={self.occupation}, headline={self.headline}, summary={self.summary}, country={self.country}, country_full_name={self.country_full_name}, city={self.city}, state={self.state})"
