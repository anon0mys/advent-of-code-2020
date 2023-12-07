

class Subscription
  def initialize
    @due_date = '2023/01/01'
    @amount_due = 100
    @amount_collected = 0
  end

  def renew!
    collect_money
    update_due_date
  end

  def update_due_date
    @due_date += 30.days
  end

  def collect_money
    @amount_collected = 100
    @amount_due = 0
  end
end

subscription = Subscription.new
subscription.renew!

subscription.amount_due == 0
subscription.due_date == '2023/02/01'


describe Subscription do
  it 'updates_due_date' do
    sub = Subscription.new

    expect(sub.due_date).to eq '2023/01/01'

    sub.update_due_date

    expect(sub.due_date).to eq '2023/02/01'
  end

  it 'updates_due_date pure' do
    sub = Subscription.new

    start_date = sub.due_date
    expect(start_date).to eq '2023/01/01'

    result = sub.update_due_date(start_date)

    expect(result).to eq '2023/02/01'
  end
end