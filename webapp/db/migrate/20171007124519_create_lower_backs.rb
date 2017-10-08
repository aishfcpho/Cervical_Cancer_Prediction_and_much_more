class CreateLowerBacks < ActiveRecord::Migration[5.1]
  def change
    create_table :lower_backs do |t|
      t.decimal :pelvic_incidence
      t.decimal :pelvic_tilt
      t.decimal :lumbar_lordosis_angle
      t.decimal :sacral_slope
      t.decimal :pelvic_radius
      t.decimal :degree_spondylolisthesis
      t.decimal :pelvic_slope
      t.decimal :Direct_tilt
      t.decimal :thoracic_slope
      t.decimal :cervical_tilt
      t.decimal :sacrum_angle
      t.decimal :scoliosis_slope
      t.string :outcome

      t.timestamps
    end
  end
end
