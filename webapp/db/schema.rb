# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20171007223227) do

  create_table "lower_backs", force: :cascade do |t|
    t.decimal "pelvic_incidence"
    t.decimal "pelvic_tilt"
    t.decimal "lumbar_lordosis_angle"
    t.decimal "sacral_slope"
    t.decimal "pelvic_radius"
    t.decimal "degree_spondylolisthesis"
    t.decimal "pelvic_slope"
    t.decimal "Direct_tilt"
    t.decimal "thoracic_slope"
    t.decimal "cervical_tilt"
    t.decimal "sacrum_angle"
    t.decimal "scoliosis_slope"
    t.string "outcome"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "user_data", force: :cascade do |t|
    t.integer "age"
    t.integer "number_of_sexual_partners"
    t.integer "first_sexual_intercourse_age"
    t.integer "number_of_pregnancies"
    t.integer "smokes"
    t.float "smokes_years"
    t.integer "hormonal_contraceptives"
    t.float "hormonal_contraceptives_years"
    t.integer "iud"
    t.integer "iud_years"
    t.integer "stds"
    t.integer "stds_number"
    t.integer "stds_condylomatosis"
    t.integer "cervical_condylomatosis"
    t.integer "vaginal_condylomatosis"
    t.integer "vulvo_perineal_condylomatosis"
    t.integer "syphilis"
    t.integer "pelvic_inflammatory"
    t.integer "genetic_herpes"
    t.integer "molluscum_contagiosum"
    t.integer "aids"
    t.integer "hiv"
    t.integer "hepatitis_b"
    t.integer "hpv"
    t.integer "number_of_diagnosis"
    t.integer "time_since_first_diagnosis"
    t.integer "time_since_last_diagnosis"
    t.integer "cancer"
    t.integer "cin"
    t.integer "dx"
    t.integer "hinselmann"
    t.integer "schiller"
    t.integer "citology"
    t.integer "biopsy"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer "sign_in_count", default: 0, null: false
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.string "current_sign_in_ip"
    t.string "last_sign_in_ip"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

end
