from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  def login_button(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  def exit_button(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here


  def back_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("back_1", "click")
  def back_1(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here
home_name = "EAGLES"
away_name = "SHARKS"
home_points = 0
away_points = 0
home_sets = 0
away_sets = 0
home_aces = 0
away_aces = 0


def buka_halaman(self, nama_halaman):
  """Fungsi untuk gonta-ganti tampilan panel halaman"""
  
  self.panel_login.visible = False
  self.panel_menu.visible = False
  self.panel_scoreboard.visible = False
  self.panel_team_settings.visible = False

 
  if nama_halaman == "login":
    self.panel_login.visible = True

  elif nama_halaman == "menu":
    self.panel_menu.visible = True

  elif nama_halaman == "scoreboard":
    self.panel_scoreboard.visible = True
    self.refresh_scoreboard()

  elif nama_halaman == "team_settings":
    self.panel_team_settings.visible = True
    self.refresh_team_settings()

  def reset_all_data_logic(self):
    """Fungsi internal untuk mengosongkan semua data game"""
    self.home_name = "EAGLES"
    self.away_name = "SHARKS"
    self.home_points = 0
    self.away_points = 0
    self.home_sets = 0
    self.away_sets = 0
    self.home_aces = 0
    self.away_aces = 0


def login_button_click(self, **event_args):
  username = self.username_box.text
  password = self.password_box.text


  if username is None or len(username) < 3:
    alert("Error: Username harus minimal 3 karakter!")
    return


  if username == "coach123" and password == "volleyball2026":
    alert("Login Berhasil!")
    self.buka_halaman("menu")
  else:
    alert("Username atau Password salah. Silakan coba lagi.")

  def exit_button_click(self, **event_args):
    alert("Aplikasi ditutup. Terima kasih!")


def view_score_board_button_click(self, **event_args):
 
  self.buka_halaman("scoreboard")
  self.plus_home_button.visible = False
  self.plus_away_button.visible = False
  self.min_home_button.visible = False
  self.min_away_button.visible = False

  def edit_teams_button_click(self, **event_args):
    self.buka_halaman("team_settings")

def update_score_button_click(self, **event_args):
  
  self.buka_halaman("scoreboard")
  self.plus_home_button.visible = True
  self.plus_away_button.visible = True
  self.min_home_button.visible = True
  self.min_away_button.visible = True

  def team_stats_button_click(self, **event_args):
    self.buka_halaman("team_settings")

def reset_button_click(self, **event_args):
  if confirm("Apakah kamu yakin ingin mereset semua data game?"):
    self.reset_all_data_logic()
    alert("Semua data berhasil di-reset!")

  def exit_app_button_click(self, **event_args):
    alert("Keluar ke halaman login.")
    self.buka_halaman("login")


def refresh_scoreboard(self):
  """Menampilkan data terbaru ke komponen scoreboard"""
  self.home_box.text = self.home_name
  self.away_box.text = self.away_name
  self.home_point_box.text = str(self.home_points)
  self.away_point_box.text = str(self.away_points)
  self.home_set_won.text = str(self.home_sets)
  self.away_set_won.text = str(self.away_sets)

  def plus_home_button_click(self, **event_args):
    self.home_points += 1
    if self.home_points >= 25:
      self.home_sets += 1
      self.home_points = 0
      self.away_points = 0
      alert(f"Set dimenangkan oleh {self.home_name}!")
    self.refresh_scoreboard()

def min_home_button_click(self, **event_args):
  if self.home_points > 0: 
    self.home_points -= 1
  self.refresh_scoreboard()

  def plus_away_button_click(self, **event_args):
    self.away_points += 1
    if self.away_points >= 25:
      self.away_sets += 1
      self.home_points = 0
      self.away_points = 0
      alert(f"Set dimenangkan oleh {self.away_name}!")
    self.refresh_scoreboard()

def min_away_button_click(self, **event_args):
  if self.away_points > 0:
    self.away_points -= 1
  self.refresh_scoreboard()

  def back_1_click(self, **event_args):
   
    self.buka_halaman("menu")


def refresh_team_settings(self):
  """Menampilkan data nama dan statistik terbaru di halaman edit"""
  self.home_name_box.text = self.home_name
  self.away_name_box.text = self.away_name
  self.home_aces_box.text = str(self.home_aces)
  self.away_aces_box.text = str(self.away_aces)

  def home_save_name_button_click(self, **event_args):
    self.home_name = self.home_name_box.text
    alert("Nama tim Home diperbarui!")

def away_save_name_button_click(self, **event_args):
  self.away_name = self.away_name_box.text
  alert("Nama tim Away diperbarui!")

  def home_team_stats_button_click(self, **event_args):
    try:
      self.home_aces = int(self.home_aces_box.text)
      alert("Statistik Aces Home diperbarui!")
    except ValueError:
      alert("Masukkan angka yang valid untuk Aces.")

def away_team_stats_button_click(self, **event_args):
  try:
    self.away_aces = int(self.away_aces_box.text)
    alert("Statistik Aces Away diperbarui!")
  except ValueError:
    alert("Masukkan angka yang valid untuk Aces.")

  def back_2_click(self, **event_args):
  
    self.buka_halaman("menu")