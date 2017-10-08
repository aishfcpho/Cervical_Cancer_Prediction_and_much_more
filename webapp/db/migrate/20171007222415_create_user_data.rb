class CreateUserData < ActiveRecord::Migration[5.1]
  def change
    create_table :user_data do |t|
      t.integer :age
      t.integer :number_of_sexual_partners
      t.integer :first_sexual_intercourse_age
      t.integer :number_of_pregnancies
      t.integer :smokes
      t.float :smokes_years
      t.integer :hormonal_contraceptives
      t.float :hormonal_contraceptives_years
      t.integer :iud
      t.integer :iud_years
      t.integer :stds
      t.integer :stds_number
      t.integer :stds_condylomatosis
      t.integer :cervical_condylomatosis
      t.integer :vaginal_condylomatosis
      t.integer :vulvo_perineal_condylomatosis
      t.integer :syphilis
      t.integer :pelvic_inflammatory
      t.integer :genetic_herpes
      t.integer :molluscum_contagiosum
      t.integer :aids
      t.integer :hiv
      t.integer :hepatitis_b
      t.integer :hpv
      t.integer :number_of_diagnosis
      t.integer :time_since_first_diagnosis
      t.integer :time_since_last_diagnosis
      t.integer :cancer
      t.integer :cin
      t.integer :hpv
      t.integer :dx
      t.integer :hinselmann
      t.integer :schiller
      t.integer :citology
      t.integer :biopsy

      t.timestamps
    end
  end
end
