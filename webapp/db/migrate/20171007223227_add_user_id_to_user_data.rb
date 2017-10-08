class AddUserIdToUserData < ActiveRecord::Migration[5.1]
  def change
    add_column :user_data, :user_id, :integer
  end
end
