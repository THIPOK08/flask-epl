from flask import Blueprint, render_template, redirect, url_for, request, flash
from epl.extensions import db
from

player_bp = Blueprint('players', __name__,template_folder='templates')

@app.route('/')
def index():
  players = db.session.scalars(db.select(Player)).all()
  return render_template('players/index.html', title='Player Page', players=players)

  @player_bp.route('/new', methods=['GET', 'POST'])
  def new_payer():
    clubs = db.session.scalars(db.select(Club)).all()
    if request.method == 'POST':
      name = request.form['name']
      position = request.form['position']
      nationality = request.form['nationality']
      goals = int(request.form['goals'])
      squad_no = int(request.form['squad_no'])
      img = request.form['img']
      club_id = int(request.form['club_id'])

      players = Player(name=name, position=position )

    return render_template('player/new_player.html', title='New Player Page', clubs=clubs)

    @app.route('/players/search', method
    def search_player():
      player_name = request.form['player_name']
      players = db.session.scalars(db.select(Player).where(Player.name.like('f%{player_name}%')))
      return render_template ('players/search_player.html',title='Player Name')
      
      @player_bp.route('/<int:id>/info')
      def info_player(id):
        player = db.session.get(Player, id)
        return render_template('players/info_player.html', title='Info Player Page', player=player)
        
         if request.method == 'POST':
      name = request.form['name']
      position = request.form['position']
      nationality = request.form['nationality']
      goals = int(request.form['goals'])
      squad_no = int(request.form['squad_no'])
      img = request.form['img']
      club_id = int(request.form['club_id'])

      player.name=name
      player.position = position
      player.nationality = nationality
      player.goals = goals
      player.squad_no = squad_no
      player.img = img
      player.club_id = club_id 

    return render_template('player/new_player.html', title='New Player Page', clubs=clubs)

    @app.route('/players/search', method
    def search_player():
      player_name = request.form['player_name']
      players = db.session.scalars(db.select(Player).where(Player.name.like('f%{player_name}%')))
      return render_template ('players/search_player.html',title='Player Name')
      
      @player_bp.route('/<int:id>/info')
      def info_player(id):
        player = db.session.get(Player, id)
        return render_template('players/info_player.html', title='Info Player Page', player=player
        
      @player_bp.route('/<int:id>/update')
      def update_player(id):
        player = db.session.get(Player, id)
        query = db.select(Club)
        clubs = db.session.scalars(query).all()
        return render_template('players/info_player.html', title='Info Player Page', player=player, clubs=clubs)