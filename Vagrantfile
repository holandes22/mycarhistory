# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "raring64"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/raring/current/raring-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.boot_timeout = 120

  config.vm.network :forwarded_port, guest: 8000, host: 8888

  config.vm.provider :virtualbox do |vb|
    vb.name = "mycarhistory"
  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
      ansible.sudo = true
      ansible.host_key_checking = false
  end

end
