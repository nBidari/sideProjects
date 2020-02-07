extends KinematicBody2D

extends Actors

onready var player_sprite: = get_node("player")
onready var anim_player: AnimationPlayer = get_node("AnimationPlayer")

#Slide
export var slide_time: = 0.4
var slide_acc: = 0.0 #slide ctr

var player_anim: = ""
var just_jumped: = false
var sliding: = false
var attacking: = false

var old_speed: = speed

func _physics_process(delta: float) -> void:
	var direction: = get_direction()
	
	if Input.is_action_pressed("slide") and velocity.x != 0 and is_on_floor():
		activate_slide_abiltiy()
	
	#Sliding
	if sliding and is_on_floor():
		slide_acc += delta
		velocity.y = 0.0
		speed.x = 250.0
		
		anim_player.play("slideCollider")
		
		if slide_acc > slide_time:
			velocity.x = 0.0
			slide_acc = 0.0
			sliding = false
			speed = old_speed
			anim_player.play("normalCollider")
			
	
	velocity = calculate_new_velocity(velocity, direction, speed)
	velocity = move_and_slide(velocity, FLOOR_NORMAL)
	player_sprite.play(player_anim)


func get_direction() -> Vector2:
	var y_direction: = 0.0
	var x_direction: = Input.get_action_strength("move_right") - Input.get_action_strength("move_left")
			
	return Vector2(
	x_direction,
	y_direction
	)

func calculate_new_velocity(
			linear_velocity: Vector2,
			direction: Vector2,
			speed: Vector2
		) -> Vector2:
	
	var new_velocity: = linear_velocity
	new_velocity.x = speed.x * direction.x
	new_velocity.y += gravity * get_physics_process_delta_time()
	
	if direction.y == -1.0:
		new_velocity.y = speed.y * direction.y
	
	return new_velocity

func activate_slide_abiltiy() -> void:
	pass

func _on_animation_finished() -> void:
	pass