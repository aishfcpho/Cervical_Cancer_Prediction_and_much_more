class UserDataController < ApplicationController
    def create
        user_data = current_user.user_data.build(user_data_params)
        if user_data.save
            # do some stuff with model here
        end
    end

    private
    def user_data_params :
        params.require(:user).permit(:age
        , :number_of_sexual_partners
        , :first_sexual_intercourse_age
        , :number_of_pregnancies
        , :smokes
        . :smokes_years
        , :hormonal_contraceptives
        ,:hormonal_contraceptives_years
        , :iud
        , :iud_years
        , :stds
        , :stds_number
        , :stds_condylomatosis
        , :cervical_condylomatosis
        , :vaginal_condylomatosis
        , :vulvo_perineal_condylomatosis
        , :syphilis
        , :pelvic_inflammatory
        , :genetic_herpes
        , :molluscum_contagiosum
        , :aids
        , :hiv
        , :hepatitis_b
        , :hpv
        , :number_of_diagnosis
        , :time_since_first_diagnosis
        , :time_since_last_diagnosis
        , :cancer
        , :cin
        , :hpv
        , :dx
        , :hinselmann
        , :schiller
        , :citology
        , :biopsy
  )
end
