import unittest
from flask import Flask,url_for
from .. import app,db,auth
from app.blog import blog_mod
from ..blog.models import Blog
from ..auth.forms import RegisterForm


class TestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		app.config.from_object('config.TestConfig')
		cls.app = app.test_client()
		cls.app_context = app.test_request_context()
		cls.app_context.push()
		db.create_all();

	@classmethod
	def tearDownClass(cls):
	 	db.session.remove()
		db.drop_all()

	def test_index_url(self):
		response = self.app.get('/')
		self.assertTrue(response.status_code,200)

	def test_addblog_url(self):
		response = self.app.get('/addBlog')
		self.assertTrue(response.status_code,401)

	def test_getblog_url(self):
		response = self.app.get('/getBlog')
		self.assertTrue(response.status_code,200)

	def test_getblogby_id_url(self):
		response = self.app.get('/getBlogById')
		self.assertTrue(response.status_code,200)

	def test_updateblog_url(self):
		response = self.app.get('/updateBlog')
		self.assertTrue(response.status_code,200)

	def test_deleteblog_url(self):
		response = self.app.get('/deleteBlog')
		self.assertTrue(response.status_code,200)
